import re

TEMPERATURE = 0
MAX_TOKENS = 500

def CLEAN_TEXT(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()