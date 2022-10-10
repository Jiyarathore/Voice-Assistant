from email.mime import audio
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning") 
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Karan . Please tell me how may I help you")           

def takeCommand():
    #it takes microphone i/p fro user and returns string o/p

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n" )

    except Exception as e:
        print(e)
        print("Say that again please..")
        return "None"    
    return query
if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)  

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")    

        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'play music' in query:
            music_dir= ' "C:\\Users\\Dell\\Downloads\\Until I Found You - Stephen Sanchez-(DJMaza).mp3"'   
            # "C:\Users\Dell\Downloads\Until I Found You - Stephen Sanchez-(DJMaza).mp3"
            # songs=os.listdir(music_dir)
            print(music_dir)
            os.startfile(music_dir)

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}") 

        elif 'open code' in query:
            vscodepath="C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(vscodepath)