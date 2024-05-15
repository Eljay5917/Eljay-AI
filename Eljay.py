import pyttsx3 #for txt to speech recognition
import datetime
import speech_recognition as sr
 
engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S") 
    speak("the current time is")
    speak(Time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)
    speak('the current date is')
    speak(day)
    speak(month)
    speak(year)
    
def wishme():
    speak('welcome back sir')
   
    time()
    
    date()
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("goodmorning sir ")
    elif hour>=12 and hour<=18:
        speak ("good afternoon sir ")
    else :
        speak("good night sir ")
        
    speak('Eljay at your service please tell me how i can help you')    
    
def takeCommand():
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
    
if __name__ =="__main__":
    wishme = ()
    while True:
        query=takeCommand().lower() 
        
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif if "wikipedia" in query:
            speak('searching.....')
            query= query.replace('wikipedia',"")
            result= wikipedia.search(query,sentences=2)
            print(result)
            speak(result)
        elif 'oflline' or 'sleep' or 'shutdown' in query:
            quit()
        elif 'lg' or "eljay" in query:
            wishme()
        