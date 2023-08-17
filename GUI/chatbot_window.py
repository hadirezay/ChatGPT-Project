from typing import Optional, Tuple, Union
import customtkinter as ctk

#Needed imports
# SQLAlchemy for inserting data into the database
# Import for openAI API, in order to load and start the chat, as well as to set appropriate parameters


class chatbot_window(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        greeting = ctk.CTkLabel(
            self,
            text="Chat Bot Module"
        ).pack()

        model_btn = ctk.CTkButton(
            self,
            text="Model Version",
            command=self.model_select
        ).pack()

        param_btn = ctk.CTkButton(
            self,
            text="Modify Parameters",
            command=self.modify_param
        ).pack()

        execute_btn = ctk.CTkButton(
            self, 
            text="Execute Chat", 
            command=self.start_chat
        ).pack()

    #Starts chat upon button press of the Execue Button
    def start_chat(self):
        #TODO: Clear the window
        #TODO: while true loop for the chatbot
        #TODO: Insert 

        #Iterates through every widget within the frame, then destroys it
        for widget in self.winfo_children():
            widget.destroy()
        print("Chat started")

    def model_select(self):
        print("Model")

    def modify_param(self):
        print("Modify")