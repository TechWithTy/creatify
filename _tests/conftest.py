import pytest
from unittest.mock import MagicMock

from app.core.third_party_integrations.creatify.client import CreatifyClient
from app.core.third_party_integrations.creatify.config import CreatifyConfig

@pytest.fixture
def mock_creatify_config() -> CreatifyConfig:
    """Provides a mock CreatifyConfig instance."""
    return CreatifyConfig(CREATIFY_API_KEY="test_api_key")

@pytest.fixture
def mock_creatify_client(mock_creatify_config: CreatifyConfig) -> CreatifyClient:
    """Provides a CreatifyClient instance with a mocked get_client method."""
    client = CreatifyClient(config=mock_creatify_config)
    client.get_client = MagicMock()
    return client
