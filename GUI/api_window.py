import customtkinter as ctk
from functools import partial

class api_window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ChatGPT Assistant")
        self.geometry("400x200")

        self.title_label = ctk.CTkLabel(
            self,
            text="Enter your API Key"
        ).pack()

        self.api_val = ctk.StringVar()

        self.api_entry = ctk.CTkEntry(self, textvariable=self.api_val).pack()

        self.enter_btn = ctk.CTkButton(
            self,
            text="Enter API key",
            command= partial(self.verify_key, self.api_val)
            ).pack()

    def verify_key(self, api_key):
        #TODO Verify API key via connection to API
        #TODO Throw exception if api_key isn't correct
        print(api_key.get())