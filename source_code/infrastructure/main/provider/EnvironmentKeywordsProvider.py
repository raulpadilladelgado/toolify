from source_code.domain.main.provider.KeywordsProvider import KeywordsProvider
from dotenv import load_dotenv
import os

class EnvironmentKeywordsProvider(KeywordsProvider):
    def __init__(self) -> None:
        load_dotenv()

    def get_keywords(self) -> list[str]:
        keywords = os.getenv("KEYWORDS", "")
        return keywords.split(",") if keywords else []