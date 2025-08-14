import httpx
from functools import lru_cache
from .config import CreatifyConfig

class CreatifyClient:
    def __init__(self, config: CreatifyConfig):
        self.config = config
        self.base_url = self.config.CREATIFY_API_BASE
        self.headers = {
            "Authorization": f"Bearer {self.config.CREATIFY_API_KEY}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    async def get_client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(base_url=self.base_url, headers=self.headers)

@lru_cache()
def get_creatify_client() -> CreatifyClient:
    # Lazily construct settings to avoid import-time validation
    settings = CreatifyConfig()
    return CreatifyClient(config=settings)
