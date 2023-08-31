

import httpx

from config import settings


async def fetch_email_verification(email: str) -> dict:
    api_url = f"https://api.emailable.com/v1/verify"
    params = {"email": email, "api_key": settings.MAIL_VALIDATION}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(api_url, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            print("Error:", e)
            return None


async def is_email_deliverable(verification_result: dict) -> bool:
    return verification_result.get("state") == "deliverable"


async def process_email(match):
    email_verification = await fetch_email_verification(match)
    is_deliverable = await is_email_deliverable(email_verification)
    return email_verification and is_deliverable
