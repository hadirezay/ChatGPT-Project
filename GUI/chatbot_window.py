from typing import Optional, Tuple, Union
import customtkinter as ctk
from functools import partial

#Needed imports
# SQLAlchemy for inserting data into the database
# Import for openAI API, in order to load and start the chat, as well as to set appropriate parameters


class chatbot_window(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Chatbot Module")
        self.geometry("800x600")
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
        #TODO Clear the window
        #TODO while true loop for the chatbot
        #TODO Insert 

        #Iterates through every widget within the frame, then destroys it
        self.clear_window()

        self.title("ChatBOT")
        #Text box to update the chat, also stores the chat with the API
        self.txt_box = ctk.CTkTextbox(
            self,
            height=400, 
            width=500
        ).pack()

        self.chatVal = ctk.StringVar()

        entry = ctk.CTkEntry(
            self,
            placeholder_text="Enter a chat here",
            textvariable = self.chatVal
        ).pack()

        enter_chat = ctk.CTkButton(
            self,
            text="Chat",
            command=partial(self.enter_chat, self.chatVal, self.txt_box)
        ).pack()
        

    def model_select(self):
        print("Model")
        self.clear_window()

        title_lbl = ctk.CTkLabel(
            self,
            text="ChatBot Module"
        ).pack()
        module35_btn = ctk.CTkButton(
            self,
            text="3.5"
        ).pack()
        module4_btn = ctk.CTkButton(
            self,
            text="4.0"
        ).pack()

    def modify_param(self):
        print("Modify")
        self.clear_window()

    def enter_chat(self, chatVal, txt_box):
        #TODO Enter chat as the button is pressed
        #TODO 
        text = chatVal.get()
        self.txt_box.insert("0.0", "Hello")

    # Set the version that is used bny the chatbot
    def set_version(self, ver):
        print(ver)

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()