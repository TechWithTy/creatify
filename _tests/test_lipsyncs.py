import pytest
from unittest.mock import AsyncMock, MagicMock

from app.core.third_party_integrations.creatify.api.lipsyncs import LipsyncAPI
from app.core.third_party_integrations.creatify.client import CreatifyClient

@pytest.mark.asyncio
async def test_get_lipsync_jobs(mock_creatify_client: CreatifyClient):
    lipsync_api = LipsyncAPI(client=mock_creatify_client)
    mock_response = MagicMock()
    mock_response.json.return_value = [{"id": "job_123"}]

    mock_async_client = AsyncMock()
    mock_async_client.get.return_value = mock_response

    mock_creatify_client.get_client = AsyncMock(return_value=MagicMock(__aenter__=AsyncMock(return_value=mock_async_client), __aexit__=AsyncMock()))

    result = await lipsync_api.get_lipsync_jobs()

    mock_async_client.get.assert_called_once_with("/lipsyncs/", params=None)
    assert result == [{"id": "job_123"}]

@pytest.mark.asyncio
async def test_create_lipsync_job(mock_creatify_client: CreatifyClient):
    lipsync_api = LipsyncAPI(client=mock_creatify_client)
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "job_456", "status": "processing"}

    mock_async_client = AsyncMock()
    mock_async_client.post.return_value = mock_response

    mock_creatify_client.get_client = AsyncMock(return_value=MagicMock(__aenter__=AsyncMock(return_value=mock_async_client), __aexit__=AsyncMock()))

    options = {"audio_url": "https://example.com/audio.mp3"}
    result = await lipsync_api.create_lipsync_job(options)

    mock_async_client.post.assert_called_once_with("/lipsyncs/", json=options)
    assert result == {"id": "job_456", "status": "processing"}

@pytest.mark.asyncio
async def test_get_lipsync_job(mock_creatify_client: CreatifyClient):
    lipsync_api = LipsyncAPI(client=mock_creatify_client)
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "job_789", "status": "succeeded"}

    mock_async_client = AsyncMock()
    mock_async_client.get.return_value = mock_response

    mock_creatify_client.get_client = AsyncMock(return_value=MagicMock(__aenter__=AsyncMock(return_value=mock_async_client), __aexit__=AsyncMock()))

    job_id = "job_789"
    result = await lipsync_api.get_lipsync_job(job_id)

    mock_async_client.get.assert_called_once_with(f"/lipsyncs/{job_id}/")
    assert result == {"id": "job_789", "status": "succeeded"}
