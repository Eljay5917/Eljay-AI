import pyttsx3 #for txt to speech recognition
import datetime
import speech_recognition as sr
 
engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
speak("welcome back  im a Eljay how can i help you")
    
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S") 
    speak(Time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)
    
def wishme():
    speak('welcome back sir')
    speak("the current time is")
    time()
    speak('the current date is')
    date()
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("goodmorning sir ")
    elif hour>=12 and hour<=18:
        speak ("good afternoon sir ")
    else :
        speak("good night sir ")
        
    speak('Eljay at your service please tell me how i can help you')    
    
def commandTaking():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ......")
        r.pause_threshold= 1
        audio=r.listen(source)
            
            
    try:
        print("Recognizing ...")
        query=r.recognize_google(audio, language="en-in")
        print(query)
        
    except Exception as e:
        print(e)
        speak("say that again please ......... ")
            
        return "None"
        
    return query
    
