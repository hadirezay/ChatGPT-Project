import os
import openai
import time
import csv


# Below is a basic code to open the API key file which will later be modify to store key
# openai.api_key = open("keyfile.txt", "r").read().strip('\n')

# Below function is for dataset module
def call_dataset(key):
    file = open('newtext.txt', 'r')
    questions = file.readlines()
    i = 1
    for line in questions:
        openai.api_key = key
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=line,
            max_tokens=100,
            temperature=0
        )
        print("Question", i, ": ", line)
        i += 1
        print("Answer: ", response['choices'][0]['text'])
        print("\n")

#Chatbot function
def call_chat(key):
    while True:
        openai.api_key = key
        # user_input = input("User: ")
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": input("User: ")}]
        )
        response = completion.choices[0].message.content
        print("ChatGPT:", response)

# Main
print("Group 20 - OpenAI chat & completion Home Page")
API_Key = input("Insert your API KEY: ")

print("Choose module")
print("Type 1 for Chatbot")
print("Type 2 for Dataset insertion")
user_choice = input()

if user_choice == "1":
    call_chat(API_Key)
elif user_choice == "2":
    call_dataset(API_Key)
