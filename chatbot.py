import random
from gtts import gTTS
import os

from math import *
from datetime import datetime

def intitiating_bot():
    intro=["\nHey good to see you.. I am chatbot\n","Hello user hope you are doing well..I am chat bot \n "]
    return random.choice(intro)

def asking_info():
    return input("Could I know your name please :) ")


def greeting_user():
    current_time = datetime.now().time()
    current_wish = "Good morning!"
    if(current_time.hour>20):
        current_wish="Hey it is too late ! "
    elif(current_time.hour>17):
        current_wish="Good night ! "
    elif (current_time.hour >15):
        current_wish = "Good evening ! "
    elif (current_time.hour >11):
        current_wish = "Good afternoon! "
    else:
        current_wish="Good morning!"
    return current_wish

def text_to_speech():
    mytext = input("enter the word that you want it's spell : ")
    try:
        if(mytext != "quit"):
            language = "en"
            output = gTTS(text = mytext,lang=language,slow=True)
            output.save("output.mp3")
            os.system("start output.mp3")
    except Exception as e:
        print(str(e))
    print("press enter to continue or enter quit to stop")
    res=input()
    if(res=="quit"):
        return res

def bot():
    print(intitiating_bot())
    name=asking_info() 
    print("\n")
    wish= greeting_user()
    print(wish, name,)
    print("\n")
    res="notquit"
    while(res!="wholeexit"):
        print("Tasks can be done by me \n")
        print("Enter 1 : calculations")
        print("Enter 2 : Dictionary ")
        print("Enter 3 : music")
        print("Enter 4 : storytelling")
        print("Enter 5 : How to pronounce a word ")
        print("Enter 6 : To exit from chatbot\n")
        option = int(input("Enter your choice : "))
        pro="notquit"
        if(option == 1):
            from calculations import cal_exp
            res="false"
            while(res!="quit"):
                res= cal_exp()
                

        elif(option == 2):
            from calcdic import dict_bot_out
            res="false"
            while(res!="quit"):
                res=dict_bot_out()
            
            

        elif(option == 3):
            from storytelling import music
            res="false"
            while(res!="quit"):
                res=music()
        
        elif(option == 4):
            from storytelling import story_telling
            res="false"
            while(res!="quit"):
                res=story_telling()

        elif(option == 5):
            res="false"
            while(res!="quit"):
                res=text_to_speech()
        elif(option == 6):
            print("Thanks for chatting...Hope you have a great time :)")
            break
        else:
            print("Please enter valid option..")

            
            
bot()