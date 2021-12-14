import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import wolframalpha
import os
import sys
from mss import mss
import subprocess
from pynput.mouse import Button, Controller
import urllib.request
import urllib.parse
import re
import psutil

battery = psutil.sensors_battery()

mouse = Controller()

engine = pyttsx3.init()

client = wolframalpha.Client('X9U37K-XUVA43H3AK')

voices = engine.getProperty('voices')


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Try typing the command!')
        query = str(input('Command: '))

    return query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#
def initialize():
    while True:
        query = myCommand();
        query = query.lower()
        if 'open youtube' in query:
            subprocess.call(["afplay", "jarvis_asyouwish.mp3"])
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query or 'open chrome' in query:
            subprocess.call(["afplay", "jarvis_asyouwish.mp3"])
            subprocess.call(
                ["/usr/bin/open", "-W", "-n", "-a", "/Applications/Google Chrome.app"]
            )

        elif 'open gmail' in query:
            subprocess.call(["afplay", "jarvis_asyouwish.mp3"])
            webbrowser.open('https://www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'open wikipedia' in query:
            subprocess.call(["afplay", "jarvis_asyouwish.mp3"])
            webbrowser.open('https://www.wikipedia.org')

        elif 'open my drive' in query:
            subprocess.call(["afplay", "jarvis_asyouwish.mp3"])
            webbrowser.open('https://drive.google.com/drive/u/0/my-drive')

        elif 'activate lockdown' in query:
            subprocess.call(["afplay", "jarvis_stand_by.mp3"])
            sys.exit()


        elif 'close google' in query or 'close chrome' in query:
            subprocess.call(["afplay", "jarvis_asyouwish.mp3"])
            os.system("pkill Chrome")

        elif 'play music' in query:
            speak('What music would you like?')
            query_string = urllib.parse.urlencode({"search_query": (sys.stdin.readline())})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])

        elif 'how are you doing?' in query:
            speak('''I'm great sir''')

        elif 'take screenshot' in query:
            subprocess.call(["afplay", "jarvis_asyouwish.mp3"])
            with mss() as sct:
                sct.shot()
        elif 'Who are you' in query:
            speak('I am and will always be Jarvis')

        elif 'scroll down' in query:
            mouse.scroll(0, 2)

        elif 'scroll up' in query:
            mouse.scroll(0, -2)

        elif 'email' in query:
            speak('who is the recipient?')
            recipient = myCommand()
            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("", "")
                    server.sendmail("", " ", content)
                    server.close()
                    subprocess.call(["afplay", "jarvis_email_sent.mp3"])
                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak(results)

            except:
                subprocess.call(["afplay", "jarvis_access_auth.mp3"])

        speak('Next Command! Sir!')
