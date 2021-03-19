from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import subprocess
import time
import numpy as np
import face_recognition as fr
import cv2
from datetime import date
from gtts import gTTS
import playsound
from serpapi import GoogleSearch

SCOPES = [fglskhfjsdjlkfsdf]

myName = "he ki"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    tts = gTTS(text=text, lang='en-us', slow=False)
    tts.save("sam.mp3")
    playsound.playsound('sam.mp3')
    os.remove("sam.mp3")

firstTime = True


def main():
    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            audio = r.listen(source)
        try:
            print('recognizing...')
            query = r.recognize_google(audio, language = 'en-us')
            print(f"user said: {query}\n")
        except Exception as e:
            query = "None"
        return query
        
    querySam = takeCommand()

    if "Sam" in querySam:
        global firstTime
        if firstTime != False:
            speak("Hello hiki. I'm Sam your virtual assistant. Would you like to see what I can do?")
            query = takeCommand()
            if "ye" in query:
                speak("Sam stands for Super Awesome Machine. I can search the web, get events from your calendar, open apps, and many other things")
            elif "no" in query:
                speak("okay. ask me for the tutorial if you need help.")
            firstTime = False
       
        else:
            speak("Hello hiki, How can I help you")
            query = takeCommand()
            if "can you" in query:
                query.replace("can you", "")
            if 'who is' in query:
                whoIs = random.randint(0, 2)
                if whoIs == 0:
                    speak('Searching for ' + query.replace('who is', ''))
                    result = wikipedia.summary(query, sentences =2)
                    speak(result)
                if whoIs == 1:
                    result = wikipedia.summary(query, sentences =2)
                    speak(result)
                if whoIs == 2:
                    result = wikipedia.summary(query, sentences =2)
                    speak('According to wikipedia, ' + result)
            elif "who's" in query:
                whoIs = random.randint(0, 2)
                if whoIs == 0:
                    speak('Searching for ' + query.replace("who's", ''))
                    result = wikipedia.summary(query, sentences =2)
                    speak(result)
                if whoIs == 1:
                    result = wikipedia.summary(query, sentences =2)
                    speak(result)
                if whoIs == 2:
                    result = wikipedia.summary(query, sentences =2)
                    speak('According to wikipedia, ' + result)
            elif 'who are' in query:
                whoIs = random.randint(0, 2)
                if whoIs == 0:
                    speak('Searching for ' + query.replace('who are', ''))
                    result = wikipedia.summary(query, sentences =2)
                    speak(result)
                if whoIs == 1:
                    result = wikipedia.summary(query, sentences =2)
                    speak(result)
                if whoIs == 2:
                    result = wikipedia.summary(query, sentences =2)
                    speak('According to wikipedia, ' + result)
            elif 'what are' in query:
                whoIs = random.randint(0, 2)
                if whoIs == 0:
                    speak('Searching for ' + query.replace('what are', ''))
                    result = wikipedia.summary(query, sentences =2)
                    speak(result)
                if whoIs == 1:
                    result = wikipedia.summary(query, sentences =2)
                    speak(result)
                if whoIs == 2:
                    result = wikipedia.summary(query, sentences =2)
                    speak('According to wikipedia, ' + result)
            if 'what is' in query:
                if "my name" in query:
                    speak("Your name is " + myName)
                elif "class" in query:
                    service = AuthGoogle()
                    getEvents(2, service)
                else:    
                    whoIs = random.randint(0, 2)
                    if whoIs == 0:
                        speak('Searching for ' + query.replace('what is', ''))
                        result = wikipedia.summary(query, sentences =2)
                        speak(result)
                    if whoIs == 1:
                        result = wikipedia.summary(query, sentences =2)
                        speak(result)
                    if whoIs == 2:
                        result = wikipedia.summary(query, sentences =2)
                        speak('According to wikipedia, ' + result)
                    whoIs = random.randint(0, 2)
                    if whoIs == 0:
                        speak('Searching for ' + query.replace("what's", ''))
                        result = wikipedia.summary(query, sentences =2)
                        speak(result)
                    if whoIs == 1:
                        result = wikipedia.summary(query, sentences =2)
                        speak(result)
                    if whoIs == 2:
                        result = wikipedia.summary(query, sentences =2)
                        speak('According to wikipedia, ' + result)         
            if "what's" in query:
                if "my name" in query:
                    speak("Your name is " + myName)
                elif "class" in query:
                    service = AuthGoogle()
                    getEvents(2, service)
                else:    
                    whoIs = random.randint(0, 2)
                    if whoIs == 0:
                        speak('Searching for ' + query.replace('what is', ''))
                        result = wikipedia.summary(query, sentences =2)
                        speak(result)
                    if whoIs == 1:
                        result = wikipedia.summary(query, sentences =2)
                        speak(result)
                    if whoIs == 2:
                        result = wikipedia.summary(query, sentences =2)
                        speak('According to wikipedia, ' + result)
                    whoIs = random.randint(0, 2)
                    if whoIs == 0:
                        speak('Searching for ' + query.replace("what's", ''))
                        result = wikipedia.summary(query, sentences =2)
                        speak(result)
                    if whoIs == 1:
                        result = wikipedia.summary(query, sentences =2)
                        speak(result)
                    if whoIs == 2:
                        result = wikipedia.summary(query, sentences =2)
                        speak('According to wikipedia, ' + result)       
                pass     
            elif "open YouTube" in query:
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open("youtube.com")
                speak('opening youtube...')
            elif "open Schoology" in query:
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
                webbrowser.get('chrome').open("app.schoology.com")
                speak('opening school ogee...')
            elif "open Apple music" in query:
                speak('Opening Apple Music...')
                os.startfile('iTunes.exe')
            elif "open iTunes" in query:
                speak('Opening iTunes...')
                os.startfile('iTunes.exe')
                pass
            elif "open Minecraft" in query:
                speak("Opening Minecraft...")
                os.startfile("C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe")
                pass
            elif "open Chrome" in query:
                ("Opening Google Chrome...")
                os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
                pass
            elif "open Google Chrome" in query:
                speak("Opening Google Chrome...")
                os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
                pass
            elif "you there" in query:
                always = random.randint(0 ,3)
                if always == 0:
                    speak("For you sir, always")
                elif always == 1:
                    speak("Always")
                elif always == 2:
                    speak("I can't leave sir. Always here.")
                else:
                    speak("yes i am")      
            elif "how are you" in query:
                speak("i dont have feelings. I am a robot. Actually, now that i think about it, I'm sad because hiki is too lazy to finish me.")
                pass
    else:
        print("no")

def AuthGoogle():
   you cant see any of this

def getEvents(n, service):
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print(f'Getting the upcoming {n} events')
    events_result = service.events().list(calendarId='you cant see this', timeMin=now,
                                        maxResults=n, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(event['summary'])
    if "the name of my class" in event['summary']:
        speak("my class")


while True:
     main()
