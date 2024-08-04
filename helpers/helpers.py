import os
from groq import Groq
import json
import logging

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def client_init(endpoint, codes="", topic="", difficulty="", questions="", language="", input_code=""):
    logging.basicConfig(level=logging.DEBUG)
    client = Groq(api_key=os.getenv('groq_api'))
    if endpoint == "/badges":
        content = ("You are a coding assistant designed to generate educational content for programming language topics. "
                   "Your main tasks include creating introductions that explain the difficulty level and key concepts, "
                   "generating coding questions that cover various aspects of the topic, and providing structured responses "
                   "that include the question, concept introduction, syntax, and expected output. Ensure the content is comprehensive, "
                   "clear, and suitable for the specified difficulty level.")
        context_template = read_file('Badges/contextTemplate.md')
        context = context_template.replace('{{codes}}', codes)
    elif endpoint == "/skills":
        content = ("You are a coding assistant designed to generate educational content for programming language topics. "
                   "Your main tasks include creating introductions that explain the difficulty level and key concepts, "
                   "generating coding questions that cover various aspects of the topic, and providing structured responses "
                   "that include the question, syntax, example input, example output, and explanation of input and output. "
                   "Ensure the content is comprehensive, clear, and suitable for the specified difficulty level.")
        context_template = read_file('Roadmap/contextTemplate.md')
        context = context_template.replace('{{topic}}', topic).replace('{{difficulty}}', difficulty).replace('{{questions}}', questions)
    elif endpoint == "/codeai":
        content = ("You are a coding assistant designed to help users with their coding tasks. Your main tasks include analyzing code for errors, suggesting improvements, providing debugging assistance, and offering coding advice. "
                   "You can assist with multiple programming languages and ensure that the user's code is efficient, clean, and follows best practices.")
        context_template = read_file('CodeAssistant/contextTemplate.md')
        context = context_template.replace('{{language}}', language).replace('{{prompt}}', input_code)
    elif endpoint == "/job-search":
        content = ("You are a conversational assistant who helps users with their job search. Your main tasks include providing the job listings relevant to the user's query and answering any questions related to these listings.")
        context_template = read_file('JobSearch/contextTemplate.md')
        context = context_template.replace('{{prompt}}', input_code)
    else:
        content = "You are a chatbot"
        context_template = read_file('CodeAssistant/contextTemplate.md')
        context = ""

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": content
            },
            {
                "role": "user",
                "content": context + "\n\nPlease provide the output in valid JSON format and do not include any additional explanatory text."
            }
        ],
        temperature=0,
        max_tokens=2500,
        top_p=1,
        stream=True,
        stop=None,
    )

    response_content = ""
    for chunk in completion:
        response_content += chunk.choices[0].delta.content or ""

    # Log the raw response content for debugging
    logging.debug("Raw response content: %s", response_content)

    # Ensure the response is a valid JSON string
    try:
        response_json = json.loads(response_content)
    except json.JSONDecodeError:
        logging.error("Failed to decode JSON response: %s", response_content)
        response_json = {"error": "Invalid JSON response from the API"}

    return response_json
