# Flask OpenAI QA

This project is a simple Flask server that exposes an endpoint to ask a question. The server sends the question to the OpenAI API, receives the answer, and saves both the question and the answer in a PostgreSQL database. The server and the database are dockerized and run with Docker Compose. The project includes a test implemented using pytest.

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Python 3.9
- OpenAI API Key

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/eladshoham1/flask-openai-qa.git
   cd flask_openai_docker
   ```

2. Create a virtual environment and activate it:

   ```bash
   py -m venv venv
   ./venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `variables.env` file and add your OpenAI API key:

   ```env
   DATABASE_URL=postgresql_url
   OPENAI_API_KEY=your_openai_api_key
   ```

5. Build and run the Docker containers:

   ```bash
   docker compose up --build
   ```

6. Run the tests:

   ```bash
   pytest
   ```

## Usage

Send a POST request to the `/ask` endpoint with a JSON payload containing the question:

```bash
curl -X POST http://localhost:5000/ask -H "Content-Type: application/json" -d '{"question": "What is the capital of France?"}'
```
