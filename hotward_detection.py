import os 
import speech_recognition as sr
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

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
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

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube kholo' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\syedi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to isam' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "syedisam2@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend isam. I am not able to send this email")    
         

        elif 'google search' in query:
            import wikipedia as googlescrap
            query = query.replace("google seacrh", "")
            query = query.replace("google search","")
            speak("this is what i found sir")
            pywhatkit.search(query)
            try:
                result = googlescrap.summary(query,1)
                speak(result)

            except:
                speak("no speakable data found")

        elif "tell me news" in query:
            speak("please wait sir, fetching latest news")
            news()

        elif "tell me joke" in query:
            joke= pyjokes.get_joke()
            speak(joke)
        
        elif "shut down the system" in query:
            speak("shutting down the system")
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            speak("restarting the system")
            os.system("shutdown /r /t 5")


        elif "take screenshot" in query:
            speak ("sir, please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("please sir hold the screen i am taking the screenshot ")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the ss have been saved in our main folder")



        elif "exit" in query:
            speak("i am going to sleep, sir . you can call me any time ")
            break
            


while True:

    wake_Up = takeCommand()

    if 'wake up' in wake_Up:
        os.startfile('"C:\\Users\\syedi\\OneDrive\\Desktop\\jarvis\\jarvis3.py"')

    else: 
        print("nothing.....")
        
