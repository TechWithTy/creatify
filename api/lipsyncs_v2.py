from ..client import CreatifyClient

class LipsyncV2API:
    def __init__(self, client: CreatifyClient):
        self.client = client

    async def get_lipsync_v2_jobs(self, params: dict = None):
        """Get all lipsync v2 jobs."""
        async with await self.client.get_client() as client:
            response = await client.get("/lipsyncs_v2/", params=params)
            response.raise_for_status()
            return response.json()

    async def create_lipsync_v2_job(self, options: dict):
        """Create a new lipsync v2 job."""
        async with await self.client.get_client() as client:
            response = await client.post("/lipsyncs_v2/", json=options)
            response.raise_for_status()
            return response.json()

    async def get_lipsync_v2_job(self, job_id: str):
        """Get a lipsync v2 job by its ID."""
        async with await self.client.get_client() as client:
            response = await client.get(f"/lipsyncs_v2/{job_id}/")
            response.raise_for_status()
            return response.json()
