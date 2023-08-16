import customtkinter as ctk
from customtkinter import filedialog as fd

# Window is byt into class, initialised with ctk.CTk variable
class main_window(ctk.CTk):
    def __init__(self):
        super().__init__()
        greeting = ctk.CTkLabel(self, text="Chat GPT").pack()

        chatbot_btn = ctk.CTkButton(self, text="ChatBot").pack()

        dataset_btn = ctk.CTkButton(
            self, 
            text="Dataset",
            command=self.select_file
            ).pack()

    #function for selecting file
    #Only takes in .csv files as an argument
    def select_file(self):
        filetypes = (
            ('CSV Files', '*.csv'),
            ('All files', '*.')
        )

        filename = fd.askopenfile(
            title = 'Select a Dataset',
            initialdir = '/',
            filetypes=filetypes
        )

        selected_ds = filename
