# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import json
import os

def handle_response(conversation):
    api_key = os.environ['openai_key']
    openai.api_key = api_key
    model_id = 'gpt-3.5-turbo'

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": conversation},
        ]
    )
    # Print the response
    response_json = str(response)
    response_dict = json.loads(response_json)
    content = response_dict['choices'][0]['message']['content']
    clean_content = content.replace('\n\n', '\n')

    return clean_content