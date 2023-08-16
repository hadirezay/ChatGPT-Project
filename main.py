import os
import openai
import time

#openai.api_key = 

#Below is a basic code to open the API key file which will later be modify to store key
#openai.api_key = open("keyfile.txt", "r").read().strip('\n')


home_menu = (1, 2)
API_Key = input("Enter your OpenAI key: ")
#print(API_Key)

print("Choose module")
print("1 = Question Dataset")
print("2 = Chatbot")
user_choice = input()
if user_choice == 1:
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "You are a helpful assistant."}]
    )
    response = completion.choices[0].message.content
    print(response)