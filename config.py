from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix=False,
    settings_files=[".env"],
)

patterns = {
    "PHONE_NUMBER": r"(?<!\d)(?:\+|00)?(?:90|0)?[- ]?\d{3}[- ]?\d{3}[- ]?\d{2}[- ]?\d{2}(?!\d)|\+98\s?\d{3}\s?\d{3}\s?\d{4}",
    "EMAIL": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",  # <--valid-->
    "URL": r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",  # valid
    "CREDIT_CARD": r"\b\d{4}[\s\-]?\d{4}[\s\-]?\d{4}[\s\-]?\d{4}\b",  # valid
    "COMBOLIST": (
        r"\b(?:[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+:"
        r"[a-zA-Z0-9]{4,}\b)"
    ),  # valid gerek yok
    "DATE": r"\b\d{2}/\d{2}/\d{4}\b",  # valid
    "DOMAIN": r"(?<!@)\b([a-zA-Z0-9-]+\.[a-zA-Z]{2,6})(?=\s|$|,)",  # valid
    "ID_NUMBER": r"\b[1-9]\d{10}\b",  # <--valid-->
    "PLATE": r"\b([0-9]{2}[A-Z]{1,3}[0-9]{1,5})\b",  # valid gerek yok
    "HASH": r"[a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64}",
}
