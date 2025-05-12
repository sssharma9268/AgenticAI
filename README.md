# Agentic AI API

A FastAPI-based application that provides an API endpoint for OpenAI chat completions.

## Features

- FastAPI REST API with async support
- OpenAI GPT integration
- Swagger documentation
- Docker containerization
- GitHub Actions CI pipeline
- Poetry for dependency management
- Ruff for linting

## Prerequisites

- Python 3.9 or higher
- Poetry (Python package manager)
- Docker (optional, for containerization)
- OpenAI API key

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/agentic-ai.git
cd agentic-ai
```

### 2. Install Poetry

For Windows:
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

For Unix/macOS:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 3. Install dependencies

```bash
poetry install
```

Installing Git Pre-Commit Hook:
```bash
poetry run pre-commit install
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the Application

### Local Development

1. Activate the Poetry shell:
```bash
poetry shell
```

2. Run the FastAPI application:
```bash
python app.py
```

The API will be available at:
- API Endpoint: http://localhost:8080/api/chat
- Swagger Documentation: http://localhost:8080/docs
- ReDoc Documentation: http://localhost:8080/redoc

### Using Docker

1. Build the Docker image:
```bash
docker build -t agentic-ai .
```

2. Run the container:
```bash
docker run -p 8080:8080 --env-file .env agentic-ai
```

## API Usage

### Chat Completion Endpoint

**Endpoint:** `POST /api/chat`

**Request Body:**
```json
{
    "prompt": "What is the capital of France?"
}
```

**Response:**
```json
{
    "status": "success",
    "response": "The capital of France is Paris.",
    "model": "gpt-3.5-turbo"
}
```

## Development

### Running Linter

```bash
poetry run ruff check .
```

### Running Tests

```bash
# TODO: Add test commands once tests are implemented
```

## CI/CD

The project includes a GitHub Actions workflow that:
1. Builds the Docker image
2. Runs the linter
3. Executes tests (when implemented)

The workflow is triggered on:
- Push to main branch
- Pull requests to main branch

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── build.yml      # GitHub Actions workflow
├── services/
│   └── openai_service.py  # OpenAI integration service
├── .env                   # Environment variables (not in repo)
├── app.py                 # FastAPI application
├── Dockerfile            # Docker configuration
├── pyproject.toml        # Poetry configuration
└── README.md            # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[MIT License](LICENSE)
