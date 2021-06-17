FROM python:3.9

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.6

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY bot bot
COPY swagger_client swagger_client

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/bot:/usr/src/app"
WORKDIR /usr/src/app/bot
CMD [ "python", "main.py" ]