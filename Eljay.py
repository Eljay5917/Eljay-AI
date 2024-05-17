import pyttsx3 #for txt to speech recognition
import datetime
import speech_recognition as sr
import wikipedia 
import smtplib
import webbrowser as wb
import os

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Power on. welcome back,  im a Eljay, your personal assistant, how can i help you")    
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
def sendemail(to, content):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.startttls()
    server.login('elijahmawuliattakorah@gmail.com','pJsci216')
    server.sendmail('elijahmawuliattakorah@gmail.com',to, content)
    server.close()
    
    
    
            
            
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
        elif "wikipedia" or 'what' or 'why' or 'where' or 'how' or 'who' in query:
            speak('searching.....')
            query= query.replace('wikipedia',"")
            result= wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif 'search in chrome' in query:
            speak('what should i search in chrome')
            chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
            search= takeCommand().lower()
            wb.get(chromepath).open_newtab(search+'.com')
            
            
        elif "send email" in query:
            try:
                speak("what should I say?")
                content=takeCommand()
                to ='abc@gmail.com'
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak('unable to send the email')
                
        elif 'logout' in query:
            os.system('shutdown -l')
        elif 'shutdown' in query:
            os.system('shutdown /s /t l')
        elif 'restart' in query:
            os.system('shutdown /r /t l')
        
        elif 'play songs' in query:
            songs_dir = 'C:\\Users\Eljay\Videos\Video'
            songs =os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
            
        elif 'remember' in query:
            speak('what should i remember?')
            data= takeCommand()
            remember =  open('data.txt','w')
            
        elif 'oflline' or 'sleep' or 'shutdown' in query:
            speak('shutting down.....')
            quit()
       
    