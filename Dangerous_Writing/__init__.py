from customtkinter import CTk

from .controllers import MainController


class CreateApp(CTk):
    def __init__(self):
        super().__init__()

        self.minsize(width=500, height=400)
        self.config(padx=10, pady=10, )
        self.title("My App")

        self.ctrl = MainController(self)

