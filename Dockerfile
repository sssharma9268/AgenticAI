#------------------------ Base Stage ------------------------
# Base image containing project dependencies
FROM python:3.12-slim AS base

#install gcc so that python dependencies can be build if needed
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends build-essential gcc python3-dev libffi-dev libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry==1.8.4

#Set Poetry configuration
ENV POETRY_VIRTUALENVS_IN_PROJECT=true \ 
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Set working directory
WORKDIR /service

# Copy the bare miminum to install dependencies
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --without dev --no-root --sync

# Set environment variables for the runtime stage
ENV PATH="/service/.venv/bin:$PATH"

#----------------------------- Development Stage -----------------------------
# Includes dev dependencies and extra tools for local development
FROM base AS development

# Install system dependencies
RUN poetry install --with dev --no-root --sync

# Set CMD to run the app (Entrypoint allows overriding  )
ENTRYPOINT ["uvicorn"]
CMD ["app.main:app", "--host", "0.0.0.0", "--port", "8000","--no-server-header", "--reload"]

#----------------------------- Cloud Stage -----------------------------
FROM base AS cloud

#Create non-root user
RUN useradd --create-home --shell /bin/bash app-user

#Change to non-root user
USER app-user

#Copy application code into the image
COPY --chown=app-user:app-user app ./app

#Set the default command to run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--no-server-header"]
