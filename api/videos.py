from ..client import CreatifyClient

class VideoAPI:
    def __init__(self, client: CreatifyClient):
        self.client = client

    async def create_video_from_link(self, link: str, options: dict = None):
        """Create video from a link."""
        if options is None:
            options = {}
        payload = {"link": link, **options}
        async with await self.client.get_client() as client:
            response = await client.post("/link_to_videos/", json=payload)
            response.raise_for_status()
            return response.json()

    async def get_video_result(self, video_id: str):
        """Get video result by its ID."""
        async with await self.client.get_client() as client:
            response = await client.get(f"/link_to_videos/{video_id}/")
            response.raise_for_status()
            return response.json()

    async def get_video_history(self, params: dict = None):
        """Get video history."""
        async with await self.client.get_client() as client:
            response = await client.get("/link_to_videos/", params=params)
            response.raise_for_status()
            return response.json()

    async def generate_preview_video_from_link(self, link: str, options: dict = None):
        """Generate a preview video from a link."""
        if options is None:
            options = {}
        payload = {"link": link, **options}
        async with await self.client.get_client() as client:
            response = await client.post("/link_to_videos/preview_list_async/", json=payload)
            response.raise_for_status()
            return response.json()

    async def render_video_from_preview(self, video_id: str, media_job_id: str):
        """Render a video from a preview."""
        payload = {"media_job": media_job_id}
        async with await self.client.get_client() as client:
            response = await client.post(f"/link_to_videos/{video_id}/render_single_preview/", json=payload)
            response.raise_for_status()
            return response.json()
