import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import client
from openai import OpenAI


recognizer= sr.Recognizer()
engine= pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def aiprocess(command):
    client=OpenAI(api_keys="Your-Api")

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": command
        }
    ]
)

    return completion.choices[0].message.content

def processcommand(c):
    if "open google" in c.lower():
        speak("opening google")
        webbrowser.open("www.google.com")
    elif "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("www.youtube.com")
    elif "open facebook" in c.lower():
        speak("opening facebook")
        webbrowser.open("www.facebook.com")
    elif "open instagram" in c.lower():
        speak("opening instagram")
        webbrowser.open("www.instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().spilit(" ")[1, ]
        link= musicLibrary.music(song)
        webbrowser.open(link)
    elif "news" in c.lower():
        speak("opening news")
        webbrowser.speak("https://timesofindia.indiatimes.com/")
    else:
        #let OpenAI handle the request
        output= aiprocess(c)
        speak(output)
    
if __name__ == "__main__":
    speak("Initializing Jarvis....")  
    while True:
    # listen for the wake word jarvis
    
        r = sr.Recognizer()
       
        
        
        # recognize speech using google
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=1)
            word= r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("ya")

                #listen for command
                with sr.Microphone() as source:
                    print("jarvis activated")
                    audio = r.listen(source)
                    command= r.recognize_google(audio)


            processcommand(command)
        except Exception as e:
            print("error; {0}".format(e))

        
        






