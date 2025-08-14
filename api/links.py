from ..client import CreatifyClient

class LinkAPI:
    def __init__(self, client: CreatifyClient):
        self.client = client

    async def get_existing_links(self, params: dict = None):
        """Get existing links."""
        async with await self.client.get_client() as client:
            response = await client.get("/links/", params=params)
            response.raise_for_status()
            return response.json()

    async def create_link(self, url: str):
        """Create a link."""
        payload = {"url": url}
        async with await self.client.get_client() as client:
            response = await client.post("/links/", json=payload)
            response.raise_for_status()
            return response.json()

    async def update_link(self, link_id: str, options: dict):
        """Update a link."""
        async with await self.client.get_client() as client:
            response = await client.put(f"/links/{link_id}/", json=options)
            response.raise_for_status()
            return response.json()

    async def get_link_by_id(self, link_id: str):
        """Get a link by its ID."""
        async with await self.client.get_client() as client:
            response = await client.get(f"/links/{link_id}/")
            response.raise_for_status()
            return response.json()
