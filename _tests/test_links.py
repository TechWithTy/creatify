import pytest
from unittest.mock import AsyncMock, MagicMock

from app.core.third_party_integrations.creatify.api.links import LinkAPI
from app.core.third_party_integrations.creatify.client import CreatifyClient

@pytest.mark.asyncio
async def test_get_existing_links(mock_creatify_client: CreatifyClient):
    link_api = LinkAPI(client=mock_creatify_client)
    mock_response = MagicMock()
    mock_response.json.return_value = [{"id": "link_123"}]

    mock_async_client = AsyncMock()
    mock_async_client.get.return_value = mock_response

    mock_creatify_client.get_client = AsyncMock(return_value=MagicMock(__aenter__=AsyncMock(return_value=mock_async_client), __aexit__=AsyncMock()))

    result = await link_api.get_existing_links()

    mock_async_client.get.assert_called_once_with("/links/", params=None)
    assert result == [{"id": "link_123"}]

@pytest.mark.asyncio
async def test_create_link(mock_creatify_client: CreatifyClient):
    link_api = LinkAPI(client=mock_creatify_client)
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "link_456"}

    mock_async_client = AsyncMock()
    mock_async_client.post.return_value = mock_response

    mock_creatify_client.get_client = AsyncMock(return_value=MagicMock(__aenter__=AsyncMock(return_value=mock_async_client), __aexit__=AsyncMock()))

    url = "https://example.com"
    result = await link_api.create_link(url)

    mock_async_client.post.assert_called_once_with("/links/", json={"url": url})
    assert result == {"id": "link_456"}

@pytest.mark.asyncio
async def test_update_link(mock_creatify_client: CreatifyClient):
    link_api = LinkAPI(client=mock_creatify_client)
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "link_789"}

    mock_async_client = AsyncMock()
    mock_async_client.put.return_value = mock_response

    mock_creatify_client.get_client = AsyncMock(return_value=MagicMock(__aenter__=AsyncMock(return_value=mock_async_client), __aexit__=AsyncMock()))

    link_id = "link_789"
    options = {"url": "https://new-example.com"}
    result = await link_api.update_link(link_id, options)

    mock_async_client.put.assert_called_once_with(f"/links/{link_id}/", json=options)
    assert result == {"id": "link_789"}

@pytest.mark.asyncio
async def test_get_link_by_id(mock_creatify_client: CreatifyClient):
    link_api = LinkAPI(client=mock_creatify_client)
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "link_101"}

    mock_async_client = AsyncMock()
    mock_async_client.get.return_value = mock_response

    mock_creatify_client.get_client = AsyncMock(return_value=MagicMock(__aenter__=AsyncMock(return_value=mock_async_client), __aexit__=AsyncMock()))

    link_id = "link_101"
    result = await link_api.get_link_by_id(link_id)

    mock_async_client.get.assert_called_once_with(f"/links/{link_id}/")
    assert result == {"id": "link_101"}
