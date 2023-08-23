import customtkinter as ctk

class history_window(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        history_lbl = ctk.CTkLabel(
            self,
            text="Question History"
        )

    def load_history(self):
        #TODO Have 2 options as to get the questions
        #TODO 1: Store the questions judged within an array, which then be iterated over 
        #TODO 2: Open the file, check if file format is correct then iterate through the questions based on question ID
        #TODO Iterate and attach labels of questions as well as their gradings
        print("History")
        