import customtkinter as ctk

class history_window(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.title = ctk.CTkLabel(self, text="History Module", corner_radius=6)
        self.title.grid(row=0, column=0, padx=20, pady=10)

        self.history_frame_button_1=ctk.CTkButton(self, text="History Button")
        self.history_frame_button_1.grid(row=2, column=0)

        self.history_check_frame=ctk.CTkFrame(self, corner_radius=0, fg_color="grey75")
        self.history_check_frame.grid_columnconfigure(0, weight=1)
        self.history_check_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")