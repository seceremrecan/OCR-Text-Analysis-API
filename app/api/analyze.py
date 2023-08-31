import json

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse

from app.core.redis_config import redis_client
from app.utils import data_extraction, ocr
from app.utils.cache_helpers import get_md5_async
from app.validation.valid_date import validate_date

router = APIRouter()


@router.post("/analyze_image/")
async def analyze_image(file: UploadFile = File(...)):
    # Desteklenen görüntü MIME türleri
    supported_image_mimes = [
        "image/jpeg",
        "image/png",
        "image/gif",
        "image/svg+xml",
        "image/webp",
        "image/apng",
        "image/avif",
    ]

    # Dosyanın MIME türünü kontrol et
    if file.content_type not in supported_image_mimes:
        response_body = {"status": "bad request. wrong file format"}
        return JSONResponse(content=response_body, status_code=400)

    # Görselin içeriğini oku
    content = await file.read()

    # Cache'de önceden sonuç var mı kontrol et
    content_hash = get_md5_async(content)
    cached_result = redis_client.get(content_hash)

    if cached_result:
        cached_result = json.loads(cached_result) # Redis'ten gelen binary veriyi stringe çevir
        return JSONResponse(content=cached_result, status_code=200)

    try:
        # Görseli OCR ile analiz edin
        extracted_text = ocr.perform_ocr(content)
        if not extracted_text:
            response_body = {"status": "No content"}
            return JSONResponse(content=response_body, status_code=204)

        # Hassas veri çıkarımını gerçekleştir
        findings = data_extraction.extract_sensitive_data(extracted_text)

        # Elde edilen sonuçları JSON formatında oluştur
        result = {
            "content": extracted_text,
            "status": "successful",
            "findings": findings,
        }

        for finding in result["findings"]:
            if finding["type"] == "DATE":
                finding["value"] = validate_date(finding["value"])

        redis_client.set(
            content_hash, json.dumps(result), ex=3600
        )  # Örnek olarak 1 saat süreyle saklayabiliriz

        return JSONResponse(content=result, status_code=200)

    except Exception as e:
        # Diğer genel hatalar için
        error_message = "Bir hata oluştu: " + str(e)
        response_body = {
            "status": "bad request. wrong file format",
            "message": error_message,
        }
        return JSONResponse(content=response_body, status_code=400)