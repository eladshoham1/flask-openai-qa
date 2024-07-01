from flask import Flask, request, jsonify, make_response
from openai_service import OpenAIService
from models import save_new_question

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    """
    Handle POST requests to the /ask endpoint.
    Expects JSON payload with a 'question' field.
    """
    try:
        data = request.get_json()
        question = data.get('question')

        if not question or not isinstance(question, str):
            return make_response(jsonify({'message': 'Invalid question'}), 400)

        status, answer = OpenAIService().ask_question(question)
        if status:
            save_new_question(question, answer)
            return make_response(jsonify({'answer': answer}), 200)
        else:
            raise Exception(answer)
    except Exception as e:
        return make_response(jsonify({'message': f'Error creating question and answer: {str(e)}'}), 500)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
