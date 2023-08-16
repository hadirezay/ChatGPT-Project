import customtkinter as ctk

# Window is byt into class, initialised with ctk.CTk variable
class main_window(ctk.CTk):
    def __init__(self):
        super().__init__()
        greeting = ctk.CTkLabel(self, text="Chat GPT").pack()