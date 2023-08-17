import customtkinter as ctk

class response_window(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

    def judge_response(self):
        print("Response judged")
        #TODO: Load question and answer text 
        #TODO: With use of SQL Alchemy, judged asnwer is inserted into the database
        #TODO: Response window will be working under a for loop, with i=1 indicating the first value
        #TODO: Exception is thrown furthermore if all appropriate fields aren't shown within the CSV/JSON File