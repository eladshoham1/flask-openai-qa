import pytest
from flask.testing import FlaskClient
from app import app

@pytest.fixture
def client() -> FlaskClient:
    with app.test_client() as client:
        yield client

def test_ask_valid_question(monkeypatch, client: FlaskClient):
    # Mock the OpenAIService and save_new_question
    class MockOpenAIService:
        def ask_question(self, question: str):
            return True, "This is a mock answer."

    def mock_save_new_question(question, answer):
        pass

    monkeypatch.setattr('openai_service.OpenAIService', MockOpenAIService)
    monkeypatch.setattr('models.save_new_question', mock_save_new_question)

    response = client.post('/ask', json={'question': 'What is the capital of France?'})
    
    assert response.status_code == 200
    assert response.json == {'answer': 'This is a mock answer.'}

def test_ask_invalid_question(client: FlaskClient):
    response = client.post('/ask', json={'question': 123})
    
    assert response.status_code == 400
    assert response.json == {'message': 'Invalid question'}

def test_ask_openai_error(monkeypatch, client: FlaskClient):
    # Mock the OpenAIService to simulate an error
    class MockOpenAIService:
        def ask_question(self, question: str):
            return False, "Mock error from OpenAI."

    monkeypatch.setattr('openai_service.OpenAIService', MockOpenAIService)

    response = client.post('/ask', json={'question': 'What is the capital of France?'})
    
    assert response.status_code == 500
    assert response.json == {'message': 'Error creating question and answer: Mock error from OpenAI.'}
