import json


class Message:
    def __init__(self, role, content):
        self.role = role
        self.content = content

    def __str__(self):
        return f"Role: {self.role}, Content: {self.content}"

    def __eq__(self, other):
        if not isinstance(other, Message):
            return NotImplemented
        return self.role == other.role and self.content == other.content


class ChatGPT:
    def __init__(self, id, model, messages):
        self.id = id
        self.model = model
        self.messages = messages  # This is a list of Message objects

    def __str__(self):
        messages_str = ', '.join(str(message) for message in self.messages)
        return f"ID: {self.id}, Model: {self.model}, Messages: [{messages_str}]"

    def __eq__(self, other):
        if not isinstance(other, ChatGPT):
            return NotImplemented
        return self.id == other.id and self.model == other.model and self.messages == other.messages

def create_chat_gpt_objects(chat_data):
    # Parse the JSON string into a Python object
    chat_data = json.loads(chat_data)

    # Create a single ChatGPT object from chat data
    return ChatGPT(
        chat_data['id'], 
        chat_data['model'], 
        [Message(choice['message']['role'], choice['message']['content']) for choice in chat_data['choices']]
    )


def search_messages(chat_gpt_objects, search_term):
    return [obj for obj in chat_gpt_objects if any(search_term.lower() in message.content.lower() for message in obj.messages)]

def main():
    # Load the JSON data
    with open('chat_data.json', 'r') as f:
        chat_data = f.read()

    # Create a ChatGPT object from the JSON data
    chat_gpt_object = create_chat_gpt_objects(chat_data)

    # Get a search term from the user
    search_term = input("Enter a search term: ")

    # Search for the term in the messages
    search_results = search_messages([chat_gpt_object], search_term)  # Wrap chat_gpt_object in a list

    # Print the results
    print("\nSearch Results:")
    for chat_gpt in search_results:
        print(chat_gpt)


if __name__ == "__main__":
    main()
