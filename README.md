# Creatify Python SDK (Internal)

Asynchronous, minimal SDK for the Creatify API used by this backend. Provides typed configuration, an async HTTP client, and resource-specific API wrappers.

- Package root: `app/core/third_party_integrations/creatify/`
- Implemented APIs: `links`, `videos`, `lipsyncs` (v1), `lipsyncs_v2`
- Test suite: `app/core/third_party_integrations/creatify/_tests/` (15 tests)

## Quick Start

1) Install dependencies (from `backend/`):
```bash
uv run python -V  # ensures venv
uv run pytest -q  # optional: verify
```

2) Configure environment:
- Set `CREATIFY_API_KEY` (required when you actually make API calls).
- Optional `.env` file in `app/core/third_party_integrations/creatify/` or project root.

Example `.env`:
```
CREATIFY_API_KEY=your-api-key
CREATIFY_API_BASE=https://api.creatify.ai/v1
```

Note: The settings loader ignores unrelated env vars and is lazy-loaded to avoid import-time failures during tests.

## Configuration
- File: `creatify/config.py`
- Model: `CreatifyConfig(BaseSettings)`
- Important fields:
  - `CREATIFY_API_KEY: str` (required for real requests)
  - `CREATIFY_API_BASE: str = "https://api.creatify.ai/v1"`
- Use `get_settings()` for lazy, cached settings construction.

## Client
- File: `creatify/client.py`
- Class: `CreatifyClient`
- Factory: `get_creatify_client()` lazily builds with `CreatifyConfig`.
- Under the hood: `httpx.AsyncClient` with `Authorization: Bearer <key>`.

## APIs
All APIs are async and require a `CreatifyClient` instance.

### Links API
- File: `creatify/api/links.py`
- Class: `LinkAPI`
- Methods:
  - `get_existing_links(params: dict | None = None)` → list
  - `create_link(url: str)` → created link JSON
  - `update_link(link_id: str, options: dict)` → updated link JSON
  - `get_link_by_id(link_id: str)` → link JSON

Usage:
```python
from app.core.third_party_integrations.creatify.client import CreatifyClient
from app.core.third_party_integrations.creatify.config import get_settings
from app.core.third_party_integrations.creatify.api.links import LinkAPI

settings = get_settings()
client = CreatifyClient(config=settings)
links = LinkAPI(client)
# await links.get_existing_links()
```

### Videos API
- File: `creatify/api/videos.py`
- Class: `VideoAPI`
- Methods:
  - `create_video_from_link(link: str, options: dict | None = None)`
  - `get_video_result(video_id: str)`
  - `get_video_history(params: dict | None = None)`
  - `generate_preview_video_from_link(link: str, options: dict | None = None)`
  - `render_video_from_preview(video_id: str, media_job_id: str)`

### Lipsync API (v1)
- File: `creatify/api/lipsyncs.py`
- Class: `LipsyncAPI`
- Methods:
  - `get_lipsync_jobs(params: dict | None = None)`
  - `create_lipsync_job(options: dict)`
  - `get_lipsync_job(job_id: str)`

### Lipsync API (v2)
- File: `creatify/api/lipsyncs_v2.py`
- Class: `LipsyncV2API`
- Methods:
  - `get_lipsync_v2_jobs(params: dict | None = None)`
  - `create_lipsync_v2_job(options: dict)`
  - `get_lipsync_v2_job(job_id: str)`

## Testing
- Suite path: `app/core/third_party_integrations/creatify/_tests/`
- Run from `backend/`:
```bash
uv run pytest app/core/third_party_integrations/creatify/_tests/
```
- Tests mock `httpx.AsyncClient` calls; no real network or API key required. Absolute imports are used for reliable discovery.

## Patterns & Notes
- Async everywhere. Use `await` and `async with` for client context.
- `response.raise_for_status()` used before returning `.json()`.
- Keep options payloads as simple dicts; the SDK is a thin transport layer.
- Additional API modules exist as placeholders; implement similarly to current modules and add tests.

## Extending the SDK
1) Create a new module under `creatify/api/` with a class similar to `LinkAPI`.
2) Add async methods that call the Creatify endpoint(s) using the shared client.
3) Write tests in `_tests/` mirroring the mocking pattern used in existing tests.
4) Run `uv run pytest` and ensure all pass.

## Troubleshooting
- Import errors during pytest collection: ensure tests use absolute imports (done in repo).
- Env validation errors: the settings are lazy and ignore extra env vars; set `CREATIFY_API_KEY` only when making real requests.
- Windows shell env var:
  - PowerShell: `$env:CREATIFY_API_KEY = 'dummy'`
  - CMD: `set CREATIFY_API_KEY=dummy`
  - Bash/Git Bash: `export CREATIFY_API_KEY=dummy`

---
Maintained by the backend team. PRs welcome for new endpoints and tests.
