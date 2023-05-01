import requests
import json
import os

from ChatGPT import ChatGPT

def connect_to_chat_gpt():
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
    }

    data = {
        "prompt": "Translate the following English text to French: '{}'",
        "max_tokens": 60
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    return response.json()

def read_chat_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def create_chat_gpt_objects(chat_data):
    return [ChatGPT(item['id'], item['model'], item['choices']) for item in chat_data]

def search_chat_gpt_objects(chat_gpt_objects, search_term):
    return [obj for obj in chat_gpt_objects if search_term in obj.__str__()]

def main():
    # Get chat data from the API
    chat_data = connect_to_chat_gpt()

    # Save chat data into a JSON file
    with open('chat_data.json', 'w') as f:
        json.dump(chat_data, f)

    # Read chat data from JSON file
    chat_data = read_chat_data('chat_data.json')

    # Create ChatGPT objects from chat data
    chat_gpt_objects = create_chat_gpt_objects(chat_data)

    # Prompt user to enter a search term
    search_term = input('Enter a search term: ')

    # Search for the term in the list of ChatGPT objects
    results = search_chat_gpt_objects(chat_gpt_objects, search_term)

    # Output the results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
