FROM python:3.10-slim as base

ARG POETRY_VERSION=1.5.1

ENV APP_DIR='/opt/app'

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # Poetry
    POETRY_HOME='/opt/poetry' \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=${POETRY_VERSION} \
    POETRY_CACHE_DIR='/opt/.cache/pypoetry' \
    POETRY_VIRTUALENVS_IN_PROJECT=true

# System dependencies
RUN apt-get -qy update \
    && apt-get install --no-install-recommends -y curl build-essential gcc ffmpeg \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get remove -y curl build-essential \
    && apt-get autoremove --purge -y \
    && apt-get autoclean -y \
    && rm -rf /var/cache/apt/* /var/lib/apt/lists/*

ENV PATH="${POETRY_HOME}/bin:${PATH}"

RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}

COPY pyproject.toml poetry.lock ${APP_DIR}/

RUN poetry --version \
    && poetry install --no-ansi --no-root --without dev -v \
    && rm -rf ${POETRY_CACHE_DIR} \
    && poetry env info --path

ENV PATH="${VIRTUAL_ENV}:${VIRTUAL_ENV}/bin:${PATH}"

COPY . ${APP_DIR}
WORKDIR ${APP_DIR}

EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
