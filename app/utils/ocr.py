import io
import pytesseract
from PIL import Image


def perform_ocr(image_content: bytes) -> str:
    """
    Görsel içeriğinden metin çıkarma işlevi.

    Parametreler:
    - image_content (bytes): Görsel içeriği (byte formatında)

    Sonuç:
    - str: Görselden çıkarılan metin
    """
    # Görsel içeriğini Image objesine dönüştür
    image = Image.open(io.BytesIO(image_content))

    # pytesseract ile metni çıkar
    text = pytesseract.image_to_string(image)

    return text.strip()
