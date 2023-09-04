from typing import Optional, Tuple, Union
import customtkinter as ctk
from functools import partial
import openai

#Needed imports
# SQLAlchemy for inserting data into the database
# Import for openAI API, in order to load and start the chat, as well as to set appropriate parameters

class chatbot_window(ctk.CTkFrame):
    def __init__(self, master, api_key):
        super().__init__(master)

        self.api_key = api_key

        self.query_label=ctk.CTkLabel(
            self,
            anchor="w",
            height=50, 
            text="Enter Querry", 
            font=("Arial", 16))
        
        self.query_label.grid(row=0, column=0)

        self.query_text = ctk.CTkTextbox(
            self, 
            border_color="black", 
            border_width=2
        )
        self.query_text.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")
        
        self.chat_frame_button_submit=ctk.CTkButton(
            self, 
            text="Submit",
            command=self.submit_text
        )
        self.chat_frame_button_submit.grid(row=2, column=0, sticky="n")
        
        self.input_param_frame=ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.input_param_frame.grid_columnconfigure(0, weight=1)
        self.input_param_frame.grid(row=1, column=1, padx=5, pady=45, sticky="nsew")
        
        # Parameter frame

        self.param_label=ctk.CTkLabel(self.input_param_frame, width=200, anchor="w", height=50, text="Parameters", font=("Arial", 16))
        self.param_label.grid(row=1, column=0)
        self.param_text=ctk.CTkTextbox(self.input_param_frame, width=200, height=50, corner_radius=2, border_color="black", border_width=2 )
        self.param_text.grid(row=2, column=0, pady=5, sticky="n" )
        self.model_label=ctk.CTkLabel(self.input_param_frame, width=200, anchor="w", height=50, text="GPT Model", font=("Arial", 16))
        self.model_label.grid(row=3, column=0)
        self.model_select_menu = ctk.CTkOptionMenu(self.input_param_frame, values=["gpt-3.5-turbo", "gpt-4"])
        self.model_select_menu.grid(row=4, column=0, pady=5, sticky="w" )

        # Response frame

        self.response_frame=ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.response_frame.grid_columnconfigure(0, weight=1)
        self.response_frame.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")
        self.response_label=ctk.CTkLabel(self.response_frame, anchor="w", height=50, text="Querry Response", font=("Arial", 16))
        self.response_label.grid(row=0, column=0)
        self.response_text = ctk.CTkTextbox(self.response_frame, border_color="black", border_width=2)
        self.response_text.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")
        self.response_text.configure(state="disabled")
        
        self.response_frame_button_submit=ctk.CTkButton(self.response_frame, text="Save & Clear",state="disabled")
        self.response_frame_button_submit.grid(row=4, column=0, pady=10, sticky="n")

        self.rate_select_menu = ctk.CTkOptionMenu(self, values=["Rating","0","1", "2","3","4","5"])
        self.rate_select_menu.grid(row=3, column=1, pady=5, sticky="w" )
    

    def submit_text(self):
        openai.api_key = self.api_key
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Say Hello",
            max_tokens=100,
            temperature=0
        )

        print("Answer: ", response['choices'][0]['text'])

