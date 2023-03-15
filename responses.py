# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import json
import os

def handle_response(conversation):
    api_key = os.environ['openai_key']
    openai.api_key = api_key
    model_id = 'gpt-3.5-turbo'

    try:
        response = openai.ChatCompletion.create(
            model=model_id,
            messages=[
                {"role": "assistant", "content": conversation},
            ]
        )
        # Print the response
        response_json = str(response)
        response_dict = json.loads(response_json)
        content = response_dict['choices'][0]['message']['content']
        clean_content = content.replace('\n\n', '\n')
        return clean_content
    
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return "Sorry, I'm having trouble understanding you right now."

'''class Chat:
    def __init__(self):
        # Setting the API key to use the OpenAI API
        api_key = os.environ['openai_key']
        openai.api_key = api_key
        self.messages = [
            {"role": "system", "content": "You are a general assistant bot to provide information to users."},
        ]

    def handle_response(self, conversation):
        self.messages.append({"role": "user", "content": conversation})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        self.messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})

        # Print the response
        response_json = str(response)
        response_dict = json.loads(response_json)
        content = response_dict['choices'][0]['message']['content']
        clean_content = content.replace('', '')
        return clean_content'''