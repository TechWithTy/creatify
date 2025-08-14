import pytest
from unittest.mock import AsyncMock, MagicMock

from app.core.third_party_integrations.creatify.api.videos import VideoAPI
from app.core.third_party_integrations.creatify.client import CreatifyClient

@pytest.mark.asyncio
async def test_create_video_from_link(mock_creatify_client: CreatifyClient):
    video_api = VideoAPI(client=mock_creatify_client)
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "video_123", "status": "processing"}
    
    mock_async_client = AsyncMock()
    mock_async_client.post.return_value = mock_response
    
    mock_creatify_client.get_client = AsyncMock(return_value=MagicMock(__aenter__=AsyncMock(return_value=mock_async_client), __aexit__=AsyncMock()))

    link = "https://example.com/video.mp4"
    result = await video_api.create_video_from_link(link)

    mock_async_client.post.assert_called_once_with("/link_to_videos/", json={"link": link})
    assert result == {"id": "video_123", "status": "processing"}

@pytest.mark.asyncio
async def test_get_video_result(mock_creatify_client: CreatifyClient):
    video_api = VideoAPI(client=mock_creatify_client)
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "video_123", "status": "succeeded"}

    mock_async_client = AsyncMock()
    mock_async_client.get.return_value = mock_response

    mock_creatify_client.get_client = AsyncMock(return_value=MagicMock(__aenter__=AsyncMock(return_value=mock_async_client), __aexit__=AsyncMock()))

    video_id = "video_123"
    result = await video_api.get_video_result(video_id)

    mock_async_client.get.assert_called_once_with(f"/link_to_videos/{video_id}/")
    assert result == {"id": "video_123", "status": "succeeded"}

@pytest.mark.asyncio
async def test_get_video_history(mock_creatify_client: CreatifyClient):
    video_api = VideoAPI(client=mock_creatify_client)
    mock_response = MagicMock()
    mock_response.json.return_value = [{"id": "video_123"}]

    mock_async_client = AsyncMock()
    mock_async_client.get.return_value = mock_response

    mock_creatify_client.get_client = AsyncMock(return_value=MagicMock(__aenter__=AsyncMock(return_value=mock_async_client), __aexit__=AsyncMock()))

    result = await video_api.get_video_history()

    mock_async_client.get.assert_called_once_with("/link_to_videos/", params=None)
    assert result == [{"id": "video_123"}]

@pytest.mark.asyncio
async def test_generate_preview_video_from_link(mock_creatify_client: CreatifyClient):
    video_api = VideoAPI(client=mock_creatify_client)
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "preview_123"}

    mock_async_client = AsyncMock()
    mock_async_client.post.return_value = mock_response

    mock_creatify_client.get_client = AsyncMock(return_value=MagicMock(__aenter__=AsyncMock(return_value=mock_async_client), __aexit__=AsyncMock()))

    link = "https://example.com/video.mp4"
    result = await video_api.generate_preview_video_from_link(link)

    mock_async_client.post.assert_called_once_with("/link_to_videos/preview_list_async/", json={"link": link})
    assert result == {"id": "preview_123"}

@pytest.mark.asyncio
async def test_render_video_from_preview(mock_creatify_client: CreatifyClient):
    video_api = VideoAPI(client=mock_creatify_client)
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "render_123"}

    mock_async_client = AsyncMock()
    mock_async_client.post.return_value = mock_response

    mock_creatify_client.get_client = AsyncMock(return_value=MagicMock(__aenter__=AsyncMock(return_value=mock_async_client), __aexit__=AsyncMock()))

    video_id = "video_123"
    media_job_id = "media_job_456"
    result = await video_api.render_video_from_preview(video_id, media_job_id)

    mock_async_client.post.assert_called_once_with(f"/link_to_videos/{video_id}/render_single_preview/", json={"media_job": media_job_id})
    assert result == {"id": "render_123"}
