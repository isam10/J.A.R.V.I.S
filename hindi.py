from platform import architecture
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import requests
import pyjokes
import pyautogui
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("शुभ प्रभात!")

    elif hour>=12 and hour<18:
        speak("नमस्कार!")   

    else:
        speak("नमस्ते!")  

    speak("मैं एलेक्सा हूं। महोदय, कृपया मुझे बताएं कि मैं आपकी कैसे मदद कर सकता हूं")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='hi')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("कृपया, दोबारा कहो...")  
        return "None"
    query = query.lower()
    return query

def news():
    main_url = 'https://newsapi.org/v2/everything?q=tesla&from=2021-10-10&sortBy=publishedAt&apiKey=f5384ba5eb1a473194ec58e2fbc18fdd'
    
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eight","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's{day[i]} news is: {head[i]}")
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

