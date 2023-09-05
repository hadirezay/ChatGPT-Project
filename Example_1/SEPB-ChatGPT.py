import customtkinter
import tkinter
import os
from PIL import Image
import sys
import openai
import mysql.connector
import ctypes
from tkinter import messagebox

# Set some global vars
mysql_host = "localhost"
user_id = ""
password =""
mydb = None
openai.api_key = "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"


customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("ChatGPT Assistant")
        self.geometry("1024x700")
        customtkinter.set_appearance_mode("system")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icons")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "chatgpt.png")), size=(26, 26))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_mono_light.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_mono_dark.png")), size=(20, 20))
        self.settings_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "settings_light2.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "settings_dark2.png")), size=(20, 20))
        self.history_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "history_light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "history_dark.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  CHATGPT Assistant", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("lightsteelblue", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event, state="disabled")
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.chat_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="ChatGPT",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("lightsteelblue", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.chat_button_event, state="disabled")
        self.chat_button.grid(row=2, column=0, sticky="ew")

        self.history_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="History",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("lightsteelblue", "gray30"),
                                                      image=self.history_image, anchor="w", command=self.history_button_event, state="disabled")
        self.history_button.grid(row=3, column=0, sticky="ew")
        
        self.settings_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Settings",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("lightsteelblue", "gray30"),
                                                      image=self.settings_image, anchor="w", command=self.settings_button_event, state="disabled")
        self.settings_button.grid(row=5, column=0, sticky="ew")


        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        # self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.image_icon_image)
        # self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        # self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        # self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        # self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        # self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        # self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        # self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)
        

        # create chat_frame frame
        self.chat_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.chat_frame.grid_columnconfigure(0, weight=1)
        self.chat_frame_title_label = customtkinter.CTkLabel(self.chat_frame,  font=("Arial", 30), text="ChatBot Module")
        self.chat_frame_title_label.grid(row=0, column=0, padx=20, pady=5)
         
        #Input Frame
        self.input_frame=customtkinter.CTkFrame(self.chat_frame, corner_radius=0, fg_color="transparent")
        self.input_frame.grid_columnconfigure(0, weight=1)
        self.input_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        self.querry_label=customtkinter.CTkLabel(self.input_frame, anchor="w", height=50, text="Enter Querry", font=("Arial", 16))
        self.querry_label.grid(row=0, column=0)
        self.querry_text = customtkinter.CTkTextbox(self.input_frame, border_color="black", border_width=2)
        self.querry_text.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")
        
        self.chat_frame_button_submit=customtkinter.CTkButton(self.chat_frame, text="Submit", command=submit_text)
        self.chat_frame_button_submit.grid(row=2, column=0, sticky="n")
        
        #Input Paramater and Model Selection Frame
        self.input_param_frame=customtkinter.CTkFrame(self.chat_frame, corner_radius=0, fg_color="transparent")
        self.input_param_frame.grid_columnconfigure(0, weight=1)
        self.input_param_frame.grid(row=1, column=1, padx=5, pady=45, sticky="nsew")
        
        self.param_label=customtkinter.CTkLabel(self.input_param_frame, width=200, anchor="w", height=50, text="Parameters", font=("Arial", 16))
        self.param_label.grid(row=1, column=0)
        self.param_text=customtkinter.CTkTextbox(self.input_param_frame, width=200, height=50, corner_radius=2, border_color="black", border_width=2 )
        self.param_text.grid(row=2, column=0, pady=5, sticky="n" )
        self.model_label=customtkinter.CTkLabel(self.input_param_frame, width=200, anchor="w", height=50, text="GPT Model", font=("Arial", 16))
        self.model_label.grid(row=3, column=0)
        self.model_select_menu = customtkinter.CTkOptionMenu(self.input_param_frame, values=["gpt-3.5-turbo", "gpt-4"])
        self.model_select_menu.grid(row=4, column=0, pady=5, sticky="w" )
        
        # Response Frame
        self.response_frame=customtkinter.CTkFrame(self.chat_frame, corner_radius=0, fg_color="transparent")
        self.response_frame.grid_columnconfigure(0, weight=1)
        self.response_frame.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")
        self.response_label=customtkinter.CTkLabel(self.response_frame, anchor="w", height=50, text="Querry Response", font=("Arial", 16))
        self.response_label.grid(row=0, column=0)
        self.response_text = customtkinter.CTkTextbox(self.response_frame, border_color="black", border_width=2)
        self.response_text.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")
        self.response_text.configure(state="disabled")
        
        self.response_frame_button_submit=customtkinter.CTkButton(self.response_frame, text="Save & Clear",state="disabled", command=sql_commit)
        self.response_frame_button_submit.grid(row=4, column=0, pady=10, sticky="n")
        
        #self.rate_label=customtkinter.CTkLabel(self.chat_frame, width=200, anchor="sw", height=50, text="Rate Response", font=("Arial", 16))
        #self.rate_label.grid(row=2, column=1 )
        self.rate_select_menu = customtkinter.CTkOptionMenu(self.chat_frame, values=["Rating","0","1", "2","3","4","5"])
        self.rate_select_menu.grid(row=3, column=1, pady=5, sticky="w" )
        #self.rate_select_menu.place_configure(relx=0.75, rely=0.65 )
        
    
        # create History frame
        self.history_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.history_frame.grid_columnconfigure(0, weight=1)
        
        self.history_frame_title_label = customtkinter.CTkLabel(self.history_frame, text="Chat History")
        self.history_frame_title_label.grid(row=0, column=0, padx=20, pady=10)

        self.history_frame_button_1=customtkinter.CTkButton(self.history_frame, text="History Button")
        self.history_frame_button_1.grid(row=2, column=0)

        self.history_check_frame=customtkinter.CTkFrame(self.history_frame, corner_radius=0, fg_color="grey75")
        self.history_check_frame.grid_columnconfigure(0, weight=1)
        self.history_check_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        
##--------------------------------------create Settings frame---------------------------------------------------

        self.settings_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.settings_frame.grid_columnconfigure(0, weight=1)
        
        self.settings_frame_label = customtkinter.CTkLabel(self.settings_frame, font=("Arial", 30), text="Settings")
        self.settings_frame_label.grid(row=0, column=0, padx=20, pady=10)
        
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.settings_frame, values=["System", "Light", "Dark"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=2, column=0, pady=30 )
        self.dbreset_button=customtkinter.CTkButton(self.settings_frame, text="Reset Database", command=db_reset)
        self.dbreset_button.grid(row=6, column=0, pady=30)
        
        
##------------------------------------ Login Frame will start as default---------------------------------------
       
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.login_frame.grid_columnconfigure(0, weight=1)
        
        self.login_frame_label = customtkinter.CTkLabel(self.login_frame, font=("Arial", 30), text="Login")
        self.login_frame_label.grid(row=0, column=0, padx=20, pady=20)
        
        self.login_id_entry = customtkinter.CTkEntry(self.login_frame, placeholder_text="UserID", width=150, height=30, border_width=2, corner_radius=10)
        self.login_id_entry.grid(row=1, column=0, padx = 20, pady=10)
        self.login_pass_entry = customtkinter.CTkEntry(self.login_frame, placeholder_text="password", show="*", width=150, height=30, border_width=2, corner_radius=10)
        self.login_pass_entry.grid(row=2, column=0, padx = 20, pady=10)
        self.login_server_entry = customtkinter.CTkEntry(self.login_frame, placeholder_text="localhost", width=150, height=30, border_width=2, corner_radius=10)
        self.login_server_entry.grid(row=3, column=0, padx = 20, pady=10)
        #self.login_key_entry = customtkinter.CTkEntry(self.login_frame, placeholder_text="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", width=150, height=30, border_width=2, corner_radius=10)
        #self.login_key_entry.grid(row=5, column=0)
        
        
        self.login_button=customtkinter.CTkButton(self.login_frame, text="Login", command=self.login_test)
        self.login_button.grid(row=8, column=0, pady=10)
        
        
        
        ## ----- This is the default login frame -----
        # select default frame
        #Should check if logged in then progress to default, otherwise enter login screen
        
        self.select_frame_by_name("Login")
    
        
    def login_test(self):
        user_id = self.login_id_entry.get()
        password = self.login_pass_entry.get()
        global mysql_host
        
        # if the user entered a host name use it, otherwise use the default localhost
        if self.login_server_entry.get() == "":
            pass
        else:
            mysql_host = self.login_server_entry.get()
            
            
        #verify login detials
        try:
            global mydb
            mydb = mysql.connector.connect(host=mysql_host, user=user_id, password=password, database="ChatGPTSEPA_DB")
            if mydb.is_connected():
                print("Connected to MySQL!")
                pass
            else:
                pass
                #print("Failed to connect to MySQL")

        except mysql.connector.Error:
            print("Error: Incorrect Username, password or mysql connection error")
            messagebox.showerror("Login Failure", "Incorrect User,Password,Server details!")        
            return
            
        #enaable the mai menu buttons
        self.home_button.configure(state="normal")
        self.chat_button.configure(state="normal")
        self.history_button.configure(state="normal")
        self.settings_button.configure(state="normal")
        self.select_frame_by_name("ChatBot")



    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.chat_button.configure(fg_color=("gray75", "gray25") if name == "ChatBot" else "transparent")
        self.history_button.configure(fg_color=("gray75", "gray25") if name == "History" else "transparent")
        self.settings_button.configure(fg_color=("gray75", "gray25") if name == "settings" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "ChatBot":
            self.chat_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.chat_frame.grid_forget()
        if name == "History":
            self.history_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.history_frame.grid_forget()
        if name == "Settings":
            self.settings_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.settings_frame.grid_forget()
        if name == "Login":
            self.login_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.login_frame.grid_forget()
            
    

    def home_button_event(self):
        self.select_frame_by_name("home")

    def chat_button_event(self):
        self.select_frame_by_name("ChatBot")

    def history_button_event(self):
        self.select_frame_by_name("History")
        
    def settings_button_event(self):
        self.select_frame_by_name("Settings")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)





def submit_text():
    messages = [{"role": "system", "content": "You are a kind helpful assistant."}]
    entered_text = str(app.querry_text.get('0.0', 'end'))
    
    #lets chatch a blank querry
    if len(entered_text) <= 1:
            messagebox.showwarning("ChatBot", "Querry is Blank!")
            ctypes.windll.user32.MessageBoxW(0, "Querry is Blank!", "ChatBot", 0)        
            return
    else:
        pass
    model_ver=str(app.model_select_menu.get())
    messages.append({"role": "user", "content": entered_text})
    chat = openai.ChatCompletion.create(model=model_ver, messages=messages)
    reply = chat.choices[0].message.content

    app.response_text.configure(state="normal")
    app.response_text.insert("insert", f"{reply} \n\n")
    app.response_text.configure(state="disabled")
    app.response_frame_button_submit.configure(state="normal")
    
    param = app.param_text.get('0.0', 'end')

    sql_insert(entered_text, model_ver, param)
    
    

def sql_insert(question, model_ver, param):
    mycursor = mydb.cursor()
    sql = "INSERT INTO Questions (Question, Model_version, parameter ) VALUES (%s, %s, %s)"
    val = (question, model_ver, param)
    mycursor.execute(sql, val)
    
def sql_commit():
    
    #config rating has been enter, ie. not "rating"
    rating = app.rate_select_menu.get()
    if rating == "Rating":
            messagebox.showwarning("ChatBot", "Please Rate Response" )
            #ctypes.windll.user32.MessageBoxW(0, "Please Rate Response", "ChatBot", 0)        
            return
    else:
            pass
    
    mydb.commit()
    mycursor = mydb.cursor()
   
    question_text = str(app.querry_text.get('0.0', 'end'))
    #Q_ID = mycursor.execute( Select Question_ID FROM Questions WHERE Question = ? ", (question_text))
                            
    sql = "SELECT MAX(Question_ID) FROM Questions WHERE Question = %s" 
    val=(question_text,)
    mycursor.execute(sql, val)
    q_id = mycursor.fetchone()
    
   # the temp var epties out the queue of responses
    temp = mycursor.fetchall()
    response = str(app.response_text.get('0.0', 'end'))
    
    mycursor = mydb.cursor()
    sql = "INSERT INTO Answers (Question_ID, Answer,Grading) VALUES(%s, %s,%s)"
    val = (q_id[0], response, rating)
    mycursor.execute(sql, val)
    mydb.commit()
    #Update History
    mycursor = mydb.cursor()
    sql = "insert into History (Question_ID, Answer_ID, Question, Answer, Grading, Comments, Model_version, parameter) select Answers.Question_ID, Answers.Answer_ID, Questions.Question, Answers.Answer, Answers.Grading, Answers.Comments, Questions.Model_version, Questions.parameter from Answers, Questions where Questions.Question_ID = " + str(q_id[0]) + " and Answers.Question_ID = "  + str(q_id[0]) + " limit 1"                    
    mycursor.execute(sql)
    mydb.commit()
    
    app.response_frame_button_submit.configure(state="disabled")
    clear_response()

def clear_response():
    app.response_text.configure(state="normal")
    app.response_text.delete('1.0', 'end')
    app.response_text.configure(state="disabled")
    clear_querry()
    #messagebox.showinfo("ChatBot", "Question & Response Saved.")
    ctypes.windll.user32.MessageBoxW(0, "Question & Response Saved.", "ChatBot", 0)
    
    
def clear_querry():
    app.querry_text.delete('1.0', 'end')
    
    
def db_reset():
    
        rdb = messagebox.askokcancel("Rest DataBase", "REST DATABASE! ARE YOU SURE?")
        if rdb == False:
                return
        else:
            pass
        
        user_id = app.login_id_entry.get()
        password = app.login_pass_entry.get()
        global mysql_host
        mydb = mysql.connector.connect(host=mysql_host, user=user_id, password=password, database="ChatGPTSEPA_DB")    
        file_path="db_init.sql"
        
        cursor = mydb.cursor()

        # Read SQL commands from the file
        with open(file_path, "r") as sql_file:
            sql_commands = sql_file.read().split(';')
            
            for sql_command in sql_commands:
                if sql_command.strip():
                    cursor.execute(sql_command)

        mydb.commit()
        print("SQL commands executed successfully!")
        cursor.close()

    
    
 




if __name__ == "__main__":
    app = App()
    app.mainloop()