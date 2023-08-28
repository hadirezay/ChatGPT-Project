import customtkinter as ctk

class history_window(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.title = ctk.CTkLabel(self, text="History Module", corner_radius=6)
        self.title.grid(row=0, column=0, padx=20, pady=10)

    def load_hsitory(self):
        
        print("History")
        