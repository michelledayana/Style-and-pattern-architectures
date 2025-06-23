from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        message = self.model.get_message()
        self.view.display_message(message)
