import logging

import httpx

from config import settings


async def fetch_dns_lookup_data(domain: str) -> dict:
    """
    Fetches DNS lookup data for the given domain using the api-ninjas API.

    Args:
        domain (str): The domain to be looked up.

    Returns:
        dict: JSON data obtained from the api-ninjas API.
    """
    api_url = f"https://api.api-ninjas.com/v1/dnslookup?domain={domain}"
    headers = {"X-Api-Key": settings.API_NINJAS}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(api_url, headers=headers)
            response.raise_for_status()
            return response.json()  # <-- Burada response.json() kullanın
        except httpx.HTTPError as e:
            logging.error("Error: %s", e)
            return None


async def verify_domain(domain: str) -> bool:
    """
    Checks if the fetch_dns_lookup_data function returns a value or not for the given domain.

    Args:
        domain (str): The domain to be verified.

    Returns:
        bool: True if fetch_dns_lookup_data returns a value, indicating that the domain is valid.
    """
    result = await fetch_dns_lookup_data(domain)
    return result is not None
