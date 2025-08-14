import pytest
from unittest.mock import AsyncMock, MagicMock

from app.core.third_party_integrations.creatify.api.lipsyncs_v2 import LipsyncV2API
from app.core.third_party_integrations.creatify.client import CreatifyClient

@pytest.mark.asyncio
async def test_get_lipsync_v2_jobs(mock_creatify_client: CreatifyClient):
    lipsync_v2_api = LipsyncV2API(client=mock_creatify_client)
    mock_response = MagicMock()
    mock_response.json.return_value = [{"id": "job_v2_123"}]

    mock_async_client = AsyncMock()
    mock_async_client.get.return_value = mock_response

    mock_creatify_client.get_client = AsyncMock(return_value=MagicMock(__aenter__=AsyncMock(return_value=mock_async_client), __aexit__=AsyncMock()))

    result = await lipsync_v2_api.get_lipsync_v2_jobs()

    mock_async_client.get.assert_called_once_with("/lipsyncs_v2/", params=None)
    assert result == [{"id": "job_v2_123"}]

@pytest.mark.asyncio
async def test_create_lipsync_v2_job(mock_creatify_client: CreatifyClient):
    lipsync_v2_api = LipsyncV2API(client=mock_creatify_client)
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "job_v2_456", "status": "processing"}

    mock_async_client = AsyncMock()
    mock_async_client.post.return_value = mock_response

    mock_creatify_client.get_client = AsyncMock(return_value=MagicMock(__aenter__=AsyncMock(return_value=mock_async_client), __aexit__=AsyncMock()))

    options = {"audio_url": "https://example.com/audio_v2.mp3"}
    result = await lipsync_v2_api.create_lipsync_v2_job(options)

    mock_async_client.post.assert_called_once_with("/lipsyncs_v2/", json=options)
    assert result == {"id": "job_v2_456", "status": "processing"}

@pytest.mark.asyncio
async def test_get_lipsync_v2_job(mock_creatify_client: CreatifyClient):
    lipsync_v2_api = LipsyncV2API(client=mock_creatify_client)
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "job_v2_789", "status": "succeeded"}

    mock_async_client = AsyncMock()
    mock_async_client.get.return_value = mock_response

    mock_creatify_client.get_client = AsyncMock(return_value=MagicMock(__aenter__=AsyncMock(return_value=mock_async_client), __aexit__=AsyncMock()))

    job_id = "job_v2_789"
    result = await lipsync_v2_api.get_lipsync_v2_job(job_id)

    mock_async_client.get.assert_called_once_with(f"/lipsyncs_v2/{job_id}/")
    assert result == {"id": "job_v2_789", "status": "succeeded"}
