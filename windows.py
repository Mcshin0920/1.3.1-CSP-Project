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
from pynput.mouse import Controller
import urllib.request
import urllib.parse
import re
import requests
import main
from playsound2 import playsound
from bs4 import BeautifulSoup

mouse = Controller()

engine = pyttsx3.init()

client = wolframalpha.Client('X9U37K-XUVA43H3AK')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def myCommand():
    r = sr.Recognizer() #call recognizer
    with sr.Microphone() as source:
        print("")
        r.pause_threshold = 1
        audio = r.listen(source) #listens for voice
    try:
        query = r.recognize_google(audio, language='en-in')# listens for the voice in english
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Try typing the command!')
        query = str(input('Command: '))

    return query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def initialize():
    query = myCommand();
    query = query.lower()
    responsemsg = ["of course", "ok", "you got it boss", "Alright"]
    if 'open youtube' in query:
        speak(random.choice(responsemsg))
        webbrowser.open("https://www.youtube.com")
        main.commandrec()


    elif "what\'s up" in query or 'how are you' in query:
        stMsgs = ['Just doing my thing!', 'I am fine!', 'I am nice and full of energy']
        speak(random.choice(stMsgs))
        main.commandrec()

    elif 'open wikipedia' in query:
        speak(random.choice(responsemsg))
        webbrowser.open('https://www.wikipedia.org')
        main.commandrec()

    elif 'open my drive' in query:
        speak(random.choice(responsemsg))
        webbrowser.open('https://drive.google.com/drive/u/0/my-drive')
        main.commandrec()

    elif 'exit' in query:
        sys.exit()

    elif 'close google' in query or 'close chrome' in query:
        speak(random.choice(responsemsg))
        os.system("pkill Chrome")
        main.commandrec()

    elif 'play music' in query:
        speak("What would you like to play?")
        musicQuery = myCommand()
        music_name = musicQuery
        query_string = urllib.parse.urlencode({"search_query": music_name})
        formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

        search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
        clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
        clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

        inspect = BeautifulSoup(clip.content, "html.parser")
        yt_title = inspect.find_all("meta", property="og:title")

        for concatMusic1 in yt_title:
            pass

        print(concatMusic1['content'])

        subprocess.Popen(
            "start /b " + "path\\to\\mpv.exe " + clip2 + " --no-video --loop=inf --input-ipc-server=\\\\.\\pipe\\mpv-pipe > output.txt",
            shell=True)
        main.commandrec()

    elif 'how are you doing?' in query:
        speak('''I'm great sir''')
        main.commandrec()

    elif 'take screenshot' in query:
        speak(random.choice(responsemsg))
        with mss() as sct:
            sct.shot()
        main.commandrec()

    elif 'who are you' in query:
        speak('I am and will always be Bob')
        main.commandrec()

    elif 'scroll down' in query:
        speak(random.choice(responsemsg))
        mouse.scroll(0, -2)
        main.commandrec()

    elif 'scroll up' in query:
        speak(random.choice(responsemsg))
        mouse.scroll(0, 2)
        main.commandrec()

    elif 'search with google' in query:
        speak("what would you like to search in google?")
        googleQuery = myCommand()
        googleQuery = googleQuery.lower()
        answer = googleQuery.split(" ")
        search = "https://www.google.com/search?q="
        x = 0
        for word in answer:
            search += "%20"
            search += answer[x]
            x = x + 1
        webbrowser.open(search)
        main.commandrec()

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
                server.login("", "") #gmail login information
                server.sendmail("", " ", content) # our email, recipient email, content
                server.close()
                playsound('jarvis_email_sent.mp3')
            except:
                speak('Sorry Sir! I am unable to send your message at this moment!')
        main.commandrec()

    else:
        query = query
        speak('Searching...')
        try:
            try:
                res = client.query(query)
                results = next(res.results).text #uses wolframalpha api to get the results
                speak('Got it.')
                speak(results)
                main.commandrec()

            except:
                results = wikipedia.summary(query, sentences=2) #uses wikipedia api to get the results
                speak('Got it.')
                speak(results)
                main.commandrec()

        except:
            playsound('jarvis_asyouwish.mp3')



