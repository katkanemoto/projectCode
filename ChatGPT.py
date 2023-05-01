class ChatGPT:
    def __init__(self, id, model, choices):
        self.id = id
        self.model = model
        self.choices = choices

    def get_id(self):
        return self.id

    def get_model(self):
        return self.model

    def get_choices(self):
        return self.choices

    def set_id(self, id):
        self.id = id

    def set_model(self, model):
        self.model = model

    def set_choices(self, choices):
        self.choices = choices

    def __str__(self):
        return f'ID: {self.id}, Model: {self.model}, Choices: {self.choices}'

    def __eq__(self, other):
        if isinstance(other, ChatGPT):
            return self.id == other.id and self.model == other.model and self.choices == other.choices
        return False
