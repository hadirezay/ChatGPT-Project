import customtkinter as ctk
import os
import openai
import time
from PIL import Image
from functools import partial
from GUI.main_window import main_window

class api_window(ctk.CTk):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.title("Enter API Key")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        #Load bg image
        current_path = os.path.dirname(os.path.realpath(__file__))

        self.bg_image = ctk.CTkImage(Image.open(
            current_path + "/bg_image/bg_image.jpg"
            ),size=(self.width, self.height))
        
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # Login Frame
        self.login_frame = ctk.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = ctk.CTkLabel(\
            self.login_frame,
            text="ChatGPT Assistant\nEnter API Key",
            font=ctk.CTkFont(size=20, weight="bold")
        ).grid(row=0, column=0, padx=30, pady=(150, 15))

        self.api_entry = ctk.CTkEntry(
            self.login_frame,
            width=200,
            placeholder_text="Enter API Key"
        ).grid(row=1, column=0, padx=30, pady=(15, 15))

        self.api_btn = ctk.CTkButton(
            self.login_frame,
            text="Verify Key",
            command=self.verify_key
        ).grid(row=2, column=0, padx=30, pady=(15, 15))


        
    def verify_key(self):
        """ openai.api_key = self.api_entry.get()
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Say Hello",
            max_tokens=100,
            temperature=0
        )

        print("Answer: ", response['choices'][0]['text']) """
        self.login_frame.grid_forget()