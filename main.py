import sys
import windows
import game
import speech_recognition as sr
from tkinter import *
from tkinter import ttk
from playsound2 import playsound
from multiprocessing import Process
from PIL import ImageTk, Image

def commandrec():
    r = sr.Recognizer()
    print("test")
    with sr.Microphone() as source:
        print("")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        heybob = r.recognize_google(audio, language='en-in')
        print('User: ' + heybob + '\n')
        heybob = heybob.lower()

        #looking for these phrases to activate the assistant
        if 'hey bob' or 'hibob' or 'k-pop' or 'a bob' in heybob:
            playsound('sound1.mp3')
            windows.initialize()
            playsound('sound2.mp3')

        else:
            commandrec()


    except sr.UnknownValueError:
        commandrec()


def gui():
    root = Tk()
    root.title("BOB")
    root.wm_attributes("-topmost", 1)

    #loading image
    load = Image.open("bob_image.jpg")
    render = ImageTk.PhotoImage(load)
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    #Placement of the labels and buttons
    ttk.Label(frm, image=render).grid(column=0, row=0)
    ttk.Label(frm, text="Quit").grid(column=0, row=2)
    ttk.Button(frm, text="Click to quit", command=sys.exit).grid(column=1, row=2)
    ttk.Label(frm, text="Play game").grid(column=0, row=1)
    ttk.Button(frm, text="Play", command=game.start).grid(column=1, row=1)
    root.mainloop()


if __name__ == "__main__":
    playsound('start.mp3')
    g = Process(target=gui)
    g.start()
    c = Process(target=commandrec)
    c.start()
    g.join()
    c.join()

