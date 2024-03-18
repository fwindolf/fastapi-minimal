# FastAPI Minimal Example

A starter App for FastAPI, no DB, no nothing.

## Installation

With poetry installed, simply run a

```
poetry install
```

## Running

To run the server, simply do a

```
set -a && source .env
poetry run uvicorn api:app --port 8000
```

During development, use hot reloading:
```
poetry run uvicorn api:app --port 8000 --reload --reload-dir .
```

## Debugging

Use the debug configuration in `.vscode/launch.json` to start debugging the server.

New environment variables for debugging should be added to that config, as well as the
`.env` file that's copied from `.env.example`.

## Deployment

No CI/CD setup, but a DockerFile and an app.json to deploy on heroku-like platforms.
