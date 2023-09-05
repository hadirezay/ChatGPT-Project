from typing import Optional, Tuple, Union
import customtkinter as ctk
from functools import partial
import openai
from Database.models import Question, Answer, History, session;
from tkinter import messagebox
import ctypes

#Needed imports
# SQLAlchemy for inserting data into the database
# Import for openAI API, in order to load and start the chat, as well as to set appropriate parameters

class chatbot_window(ctk.CTkFrame):
    def __init__(self, master, api_key):
        super().__init__(master)

        self.api_key = "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"

        self.query_label=ctk.CTkLabel(
            self,
            anchor="w",
            height=50, 
            text="Enter Query", 
            font=("Arial", 16))
        
        self.query_label.grid(row=0, column=0)

        self.query_text = ctk.CTkTextbox(
            self, 
            border_color="black", 
            border_width=2
        )
        self.query_text.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")
        
        self.chat_frame_button_submit=ctk.CTkButton(
            self, 
            text="Submit",
            command=self.submit_text
        )
        self.chat_frame_button_submit.grid(row=2, column=0, sticky="n")
        
        self.input_param_frame=ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.input_param_frame.grid_columnconfigure(0, weight=1)
        self.input_param_frame.grid(row=1, column=1, padx=5, pady=45, sticky="nsew")
        
        # Parameter frame

        self.param_label=ctk.CTkLabel(self.input_param_frame, width=200, anchor="w", height=50, text="Parameters", font=("Arial", 16))
        self.param_label.grid(row=1, column=0)
        self.param_text=ctk.CTkTextbox(self.input_param_frame, width=200, height=50, corner_radius=2, border_color="black", border_width=2 )
        self.param_text.grid(row=2, column=0, pady=5, sticky="n" )
        self.model_label=ctk.CTkLabel(self.input_param_frame, width=200, anchor="w", height=50, text="GPT Model", font=("Arial", 16))
        self.model_label.grid(row=3, column=0)
        self.model_select_menu = ctk.CTkOptionMenu(self.input_param_frame, values=["gpt-3.5-turbo", "gpt-4"])
        self.model_select_menu.grid(row=4, column=0, pady=5, sticky="w" )

        # Response frame

        self.response_frame=ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.response_frame.grid_columnconfigure(0, weight=1)
        self.response_frame.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")
        self.response_label=ctk.CTkLabel(self.response_frame, anchor="w", height=50, text="Querry Response", font=("Arial", 16))
        self.response_label.grid(row=0, column=0)
        self.response_text = ctk.CTkTextbox(self.response_frame, border_color="black", border_width=2)
        self.response_text.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")
        self.response_text.configure(state="disabled")
        
        self.response_frame_button_submit=ctk.CTkButton(self.response_frame, text="Save & Clear",state="disabled")
        self.response_frame_button_submit.grid(row=4, column=0, pady=10, sticky="n")

        self.rate_select_menu = ctk.CTkOptionMenu(self, values=["Rating","0","1", "2","3","4","5"])
        self.rate_select_menu.grid(row=3, column=1, pady=5, sticky="w" )
    

    def submit_text(self):
        messages = [{"role": "system", "content": "You are a kind helpful assistant."}]
        entered_text = str(self.query_text.get('0.0', 'end'))

        # Checks for 
        if len(entered_text) <= 1:
            messagebox.showwarning("ChatBot", "Querry is Blank!")
            ctypes.windll.user32.MessageBoxW(0, "Querry is Blank!", "ChatBot", 0)        
            return
        else:
            pass

        model_ver=str(self.model_select_menu.get())
        messages.append({"role": "user", "content": entered_text})
        chat = openai.ChatCompletion.create(model=model_ver, messages=messages)
        reply = chat.choices[0].message.content

        self.response_text.configure(state="normal")
        self.response_text.insert("insert", f"{reply} \n\n")
        self.response_text.configure(state="disabled")
        self.response_frame_button_submit.configure(state="normal")
        
        param = self.param_text.get('0.0', 'end')

        self.sql_insert(entered_text, model_ver, param)

    def sql_insert(self,question, model_ver, param):
        question_obj = Question(
            Question=question,
            Model_version=model_ver,
            parameter=param
        )

        session.add(question_obj)
        session.commit()

    def answer_insert(self):
        rating = self.rate_select_menu.get()
        if rating == "Rating":
            messagebox.showwarning("ChatBot", "Please Rate Response" )
            return
        
        # Obtain question id
        question_text = str(self.query_text.get('0.0', 'end'))
        q=session.query(Question).filter_by(Question=question_text).first()
        question_id = q.Question_ID

        response = str(self.response_text.get('0.0', 'end'))

        answer = Answer(
            Question_ID=question_id,
            Answer=response,
            Grading=rating
        )

        session.add(answer)
        session.commit()

        #Update history table
        history = History(
            Question_ID=question_id,
            Answer_ID=answer.Answer_ID,
            Question=question_text,
            Answer=response,
            Grading=rating,
            Model_version=q.Model_version,
            parameter=q.parameter
        )

        session.add(history)
        session.commit()

        self.response_frame_button_submit.configure(state="disabled")
        self.clear_response()


    def clear_query(self):
        self.query_text.delete('1.0', 'end')

    def clear_response(self):
        self.response_text.configure(state="normal")
        self.response_text.delete('1.0', 'end')
        self.response_text.configure(state="disabled")
        self.clear_query()
        messagebox.showinfo("ChatBot", "Question and Response Saved")



