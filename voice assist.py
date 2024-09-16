# Import libraries
import pyttsx3 

import datetime
 
import webbrowser

import speech_recognition as sr

def textsp(text):
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
print("hello! how may i help")
textsp("hello! how may i help")

def sptext():

 r = sr.Recognizer()

 with sr.Microphone() as source:
   print("Listening...")
   #textsp("listening...")
   r.adjust_for_ambient_noise(source)
   audio=r.listen(source) 

   try:
        text = r.recognize_google(audio)
        print("recognising...")
        print(text)

   except sr.UnknownValueError:
       print("Cannot be heard. Please say that again!")
       textsp("Cannot be heard. Please say that again!")

   if str(text).lower() == "what is your name":
              print("My name is Sky!") 
              textsp("My name is Sky!")         

   elif str(text).lower() == "how old are you":
              print("I am 1 year old")
              textsp("I am 1 year old")

   elif str(text).lower() == "can you do everything":
              print("I am still in development right now so i cannot perform a lot of tasks.")
              textsp("I am still in development right now so i cannot perform a lot of tasks.")

    # tells the time
   elif str(text).lower() == "what is the time":
              print(datetime.datetime.now().strftime('%I.%M%p'))
              textsp(datetime.datetime.now().strftime('%I.%M%p'))
    # tells the date
   elif str(text).lower() == "what is the date":
              print(datetime.datetime.now().strftime('%B-%d-%G'))
              textsp(datetime.datetime.now().strftime('%B%d%g'))

   
    # opens webbrowser
   elif str(text).lower() == "open youtube":
              webbrowser.open("http://www.youtube.com/")
              textsp("completing request...")
   elif str(text).lower() == "open google":
              webbrowser.open("http://www.google.com")
              textsp("completing request...")

sptext()

