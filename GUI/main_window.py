import customtkinter as ctk
from customtkinter import filedialog as fd
from GUI.chatbot_window import chatbot_window
from GUI.history_window import history_window

# Window is built into class, initialised with ctk.CTk variable
class main_window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Chat GPT Assistant")
        self.geometry("800x600")
        greeting_lbl = ctk.CTkLabel(
            self,
            text="Chat GPT"
        ).pack()

        chatbot_btn = ctk.CTkButton(
            self,
            text="ChatBot",
            command=self.chatbot_window
        ).pack()

        dataset_btn = ctk.CTkButton(
            self, 
            text="Dataset",
            command=self.select_file
        ).pack()
        
        history_btn = ctk.CTkButton(
            self,
            text="History",
            command=self.question_history
        ).pack()

    #Function for selecting file
    #Only takes in .csv and .json files as an argument
    def select_file(self):
        # List structure of all filetypes to be used
        # First item describes the type of file
        # Second item restricts the files to be selected to the specific extension
        filetypes = (
            ('CSV Files', '*.csv'),
            ('JSON Files', '*.json'),
            ('All files', '*.')
        )
        # Prompts user to select a file
        # Uses filetypes as a parameter for only those filetypes to be selected
        # TODO Change intiial directory to one thats in the program folder (ideally called data/datasets)

        filename = fd.askopenfile(
            title = 'Select a Dataset',
            initialdir = '/',   
            filetypes=filetypes
        )

        selected_ds = filename

        #TODO Loading of file to program
        #TODO Exception error throw if the file is corrupted
        #TODO Check csv for appropriate format, throw exception otherwise
        #TODO Load response assessment window upon file loaded and validated
        #TODO Loads response window upon successful, taking the file as an argument

    #Loads the history window of all of the recent questions assessed
    def question_history(self):
        history_window()

    # Loads the chatbot window via use of a toplevel window
    def chatbot_window(self):
        chatbot_window()
