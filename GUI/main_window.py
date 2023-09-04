import customtkinter as ctk
import openai
from customtkinter import filedialog as fd
from GUI.chatbot_window import chatbot_window
from GUI.history_window import history_window

# Window is built into class, initialised with ctk.CTk variable
class main_window(ctk.CTk):
    width = 900
    height = 600

    def __init__(self):
        super().__init__()
        self.title("ChatGPT Assistant")
        self.geometry(f"{self.width}x{self.height}")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        #Navigation frame
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="  ChatGPT Assistant",
                                                             compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                 anchor="w", command=self.home_window, state="disabled")
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.chatbot_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="ChatBot",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.chatbot_window, state="disabled")
        self.chatbot_button.grid(row=2, column=0, sticky="ew")

        self.history_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="History",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.question_history, state="disabled")
        self.history_button.grid(row=3, column=0, sticky="ew")

        # self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],)
        # self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        #Home frame
        self.home_frame = ctk.CTkFrame(
            self, 
            corner_radius=0,
            fg_color="transparent"
        )
        self.home_frame.grid(row=0, column=1, sticky="nsew")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.welcome_label = ctk.CTkLabel(
            self.home_frame,
            text="Welcome to the ChatGPT Assistant",
            width=120,
            height=25
        ).grid(row=0, column=0, padx=20, pady=10)
        
        self.enter_lbl = ctk.CTkLabel(
            self.home_frame,
            text="Enter API Key",
            width = 120,
            height=25
        ).grid(row=1, column=0, padx=20, pady=10)

        self.api_val = ctk.StringVar()

        self.api_entry = ctk.CTkEntry(
            self.home_frame,
            placeholder_text="API KEY",
            textvariable=self.api_val,
            width=150, 
            height=30, 
            border_width=2, 
            corner_radius=10
        ).grid(row=2, column=0, padx=20, pady=10)
        self.api_key = self.api_val.get()

        self.verify_button = ctk.CTkButton(self.home_frame, text="Verify Key", command=self.verify_key, fg_color="white", text_color="black")
        self.verify_button.grid(row=3, column=0, padx=20, pady=10)

        self.chatbot_frame = chatbot_window(self, self.api_key)
        self.chatbot_frame.grid_columnconfigure(0, weight=1)

        self.history_frame = history_window(self)
        self.history_frame.grid_columnconfigure(0, weight=1)

    def verify_key(self):
        api_key = self.api_val.get()
        openai.api_key = api_key
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Say Hello",
            max_tokens=100,
            temperature=0
        )

        print("Answer: ", response['choices'][0]['text'])

        # If a response is given, enable all buttons and set the API KEY as the val verified
        if response['choices'][0]['text'] != "":
            self.home_button.configure(state="enabled")
            self.chatbot_button.configure(state="enabled")
            self.history_button.configure(state="enabled")
            self.api_key = self.api_val.get()

    #Function for selecting file
    #Only takes in .csv and .json files as an argument
    # def select_file(self):
    #     # List structure of all filetypes to be used
    #     # First item describes the type of file
    #     # Second item restricts the files to be selected to the specific extension
    #     filetypes = (
    #         ('CSV Files', '*.csv'),
    #         ('JSON Files', '*.json'),
    #         ('All files', '*.')
    #     )
    #     # Prompts user to select a file
    #     # Uses filetypes as a parameter for only those filetypes to be selected
    #     # TODO Change intiial directory to one thats in the program folder (ideally called data/datasets)

    #     filename = fd.askopenfile(
    #         title = 'Select a Dataset',
    #         initialdir = '/',   
    #         filetypes=filetypes
    #     )

    #     selected_ds = filename

    #     #TODO Loading of file to program
    #     #TODO Exception error throw if the file is corrupted
    #     #TODO Check csv for appropriate format, throw exception otherwise
    #     #TODO Load response assessment window upon file loaded and validated
    #     #TODO Loads response window upon successful, taking the file as an argument

    #Loads the history window of all of the recent questions assessed
    def frame_select(self, name):
        if name == "Home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_remove()
        if name == "ChatBot":
            self.chatbot_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.chatbot_frame.grid_remove()
        if name == "History":
            self.history_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.history_frame.grid_remove()

    def home_window(self):
        self.frame_select("Home")

    # Loads the chatbot window via use of a toplevel window
    def chatbot_window(self):
        self.frame_select("ChatBot")

    def question_history(self):
        self.frame_select("History")
