from ..client import CreatifyClient

class LipsyncAPI:
    def __init__(self, client: CreatifyClient):
        self.client = client

    async def get_lipsync_jobs(self, params: dict = None):
        """Get all lipsync jobs."""
        async with await self.client.get_client() as client:
            response = await client.get("/lipsyncs/", params=params)
            response.raise_for_status()
            return response.json()

    async def create_lipsync_job(self, options: dict):
        """Create a new lipsync job."""
        async with await self.client.get_client() as client:
            response = await client.post("/lipsyncs/", json=options)
            response.raise_for_status()
            return response.json()

    async def get_lipsync_job(self, job_id: str):
        """Get a lipsync job by its ID."""
        async with await self.client.get_client() as client:
            response = await client.get(f"/lipsyncs/{job_id}/")
            response.raise_for_status()
            return response.json()
