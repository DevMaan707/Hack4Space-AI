from flask import Flask, request, jsonify
from dotenv import load_dotenv
from helpers.helpers import client_init 
from JobSearch.query import search_jobs

load_dotenv()

app = Flask(__name__)

@app.route('/generate-skill', methods=['POST'])
def generate_skill():
    data = request.json
    topic = data.get('topic')
    difficulty = data.get('difficulty')
    questions = data.get('questions')
    
    if not topic or not difficulty or not questions:
        return jsonify({'error': 'Topic, difficulty, and questions are required fields.'}), 400

    response = client_init(endpoint="/skills", topic=topic, difficulty=difficulty, questions=questions)
    return jsonify(response)

@app.route('/generate-badge', methods=['POST'])
def badge_gen():
    data = request.json
    codes = data.get('codes')
    
    if not codes or not isinstance(codes, list):
        return jsonify({'error': 'Codes must be provided as a list of strings.'}), 400

    codes_str = "\n".join(codes)
    response = client_init(endpoint="/badges", codes=codes_str)
    return jsonify(response)

@app.route('/')
def home():
    return 'Home route'

@app.route('/code-assistant', methods=['POST'])
def codeAssistant():
    data = request.json
    language = data.get('language')
    code = data.get('code')

    if not language or not code:
        return jsonify({'error': 'Invalid input, missing language or code'}), 400

    response = client_init(endpoint="/codeai", language=language, input_code=code)
    return jsonify(response)

@app.route('/job-search', methods=['POST'])
def llm_response():
    data = request.json
    query = data.get('query')
    
    if not query:
        return jsonify({'error': 'Invalid input, missing query'}), 400

    response = search_jobs(query)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
