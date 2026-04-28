# AI chat bot

import datetime
import time


name = input("Enter your name:  ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good Morning, ",name)
elif 11 <= presentHour <=17:
    print("Good Afternoon,", name)
elif  17<= presentHour >= 20:
    print("Good Evening, ", name)
else :
    print("Good night, ",name)
    

print("Namaste! Welcome To Your ChatBot")
print("You can chat with me, type 'bye' for exit...   ")

# chatbot memory creation - dict
response = {
    "hello" : "Hi, welocme. How I can help you?",
    "how are you" : "I am great, Thank you",
    "who are you" : "I am your AI chatbot",
    "motivate me" : "keep going which you love, \nnever give up on your dream, \neverything is easy only you need learn that",
    "happy" : "Wow,gld to hear that.",
    "what is python " : "it is high level programming language and can learn easily."
       
}

# function for chatbot to response
def getResponse(userQuery):
    userQuery = userQuery.lower()
    for eachkey in response:
        if eachkey in userQuery:
            return response[eachkey]
        else :
            return "I am sorry, I am not know info about this..."
            


# take user input
while True:
    userInput = input("Please ask your query..... Me: ")
    if "bye" in userInput.lower():
             break
    reply = getResponse(userInput)
    print("Bot Response : ", reply)
    

    
