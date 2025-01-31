from source_code.domain.main.provider.KeywordsProvider import KeywordsProvider


class EnvironmentKeywordsProvider(KeywordsProvider):
    def get_keywords(self) -> list[str]:
        return ["remix"]