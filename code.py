code = '''
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from playsound import playsound
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    print("Jarvis: ", audio)
    engine.say(audio)
    engine.runAndWait()


def speakWithoutSubs(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("Please tell me how may I help you")


def takeCommand():
    query = str(input("You: "))
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('maloobrothers28@gmail.com', 'maloo1008')
    server.sendmail('maloobrothers28@gmail.com', to, content)
    server.close()


def news():
    speak("English or Hindi")
    f = str(input("You: "))
    if 'english' in f:
        webbrowser.open(
            "https://epaper.hindustantimes.com/rajasthan?eddate=27/04/2021&Pageview=list")
    elif 'hindi' in f:
        webbrowser.open("https://epaper.bhaskar.com/state/rajasthan")
    else:
        speak("sorry sir i am not able to show you news!")


def countdown(time_sec):
    while time_sec:
        min = time_sec
        timeformat = '{:02d}:{:02d}'.format(0, time_sec)
        print(timeformat, end='\n',)
        speakWithoutSubs(time_sec)
        time.sleep(1)
        time_sec -= 1

    speak("Sir the time is up!")


def random(max, min):
    import random
    speak(random.randint(min, max))


if __name__ == "__main__":
    wishMe()
    while True:
        print ("Current directory is: %s" %os.getcwd())
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        friends = ["Goral", "Devendra", "Lakshaya", "Manan", "Manjeet", "Manvendra", "Naman", "Pushkar", "Ronak", "Kabir", "Kushal", "Udit", "Tarun", "Aarav", "Karan"]
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            speak("What should i search")
            b = str(input("You: "))
            query = query.replace("wikipedia", b)
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("opening open stackoverflow")

        elif 'open whitehat jr' in query:
            webbrowser.open("https://code.whitehatjr.com/s/dashboard")
            speak("Opening whitehat jr")

        elif 'who are you' in query:
            speak("I am a virtual assistant JARVIS sir! How can i help you.")

        elif 'play music' in query:
            playsound('play.wav')

        elif 'open playlist' in query:
            codePath1 = "C:\\Users\\Dhairya\\Desktop\\music library"
            os.startfile(codePath1)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f" {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'the date' in query:
            strdate = datetime.datetime.now().strftime("%D")
            print(f" {strdate}")
            speak(f"Sir, the date is {strdate}")

        elif 'the year' in query:
            strYear = datetime.datetime.now().strftime("%Y")
            print(f" {strYear}")
            speak(f"Sir, the year is {strYear}")

        elif 'open code' in query:
            codePath = "C:/Users/Dhairya/AppData/Local/Programs/Microsoft VS Code/Code"
            os.startfile(codePath)

        elif 'send a email' in query:
            try:
                speak("Whom should i send?")
                to = takeCommand()
                speak("What should i say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif 'give me you code' in query:
            speak("PLease give me the password")
            e = str(input("You: "))
            codegiving(e)

        elif 'news' in query:
            news()

        elif 'updates' in query:
            news()


        elif 'what you can do' in query:
            speak(
            'I am jarvis sir'
            'i can do many things'
            'Like telling time date year '
            'searching anything you want in wikipedia'
            'showing news'
            'giving my code'
            'sending emails to any id'
            'and more features'
            )

        elif 'what are your features' in query:
            speak(
            'I am jarvis sir'
            'i can do many things'
            'Like telling time date year '
            'searching anything you want in wikipedia'
            'showing news'
            'giving my code'
            'sending emails to any id'
            'and more features'
            )

        elif 'set timer' in query:
            speak("For how many seconds")
            h = int(input("You: "))
            countdown(h)

        elif 'random number' in query:
            speak("What should be the maximum number?")
            m = int(input("You: "))
            speak("What should be the minimum number?")
            n = int(input("You: "))
            random(m, n)

        elif 'friends' in query:
            speak(friends)

        elif 'add friend' in query:
            speak("Whom should I add ?")
            g = str(input("You: "))
            h = friends.append(g)
            speak("Added Successfully")
            print(friends)

        elif 'remove friend' in query:
            speak("Whom should I remove?")
            j = str(input("You: ")) 
            friends.remove(j)
            speak("Removed Successfully !")
            print(friends)

        elif 'add' in query:
            speak("What is the first number ?")
            a = int(input("You: "))
            speak("What should be the second number ?")
            b = int(input("You: "))
            speak(a + b)
            a= str(a)
            b = str(b)
            speak("Is the Sum of " + a + " and " + b)
        
        elif 'sum' in query:
            speak("What is the first number ?")
            a = int(input("You: "))
            speak("What should be the second number ?")
            b = int(input("You: "))
            speak(a + b)
            a= str(a)
            b = str(b)
            speak("Is the Sum of " + a + " and " + b)

        
        elif 'difference' in query:
            speak("What is the first number ?")
            a = int(input("You: "))
            speak("What should be the second number ?")
            b = int(input("You: "))
            speak(a - b)
            a= str(a)
            b = str(b)
            speak("Is the difference of " + a + " and " + b)

        elif 'subtract' in query:
            speak("What is the first number ?")
            a = int(input("You: "))
            speak("What should be the second number ?")
            b = int(input("You: "))
            speak(a - b)
            a= str(a)
            b = str(b)
            speak("Is the difference of " + a + " and " + b)

        elif 'multiply' in query:
            speak("What is the first number ?")
            a = int(input("You: "))
            speak("What should be the second number ?")
            b = int(input("You: "))
            speak(a * b)
            a= str(a)
            b = str(b)
            speak("Is the product of " + a + " and " + b)

        elif 'divide' in query:
            speak("What is the divident ?")
            a = int(input("You: "))
            speak("What should be the divisor ?")
            b = int(input("You: "))
            speak(b / a)
            a= str(a)
            b = str(b)
            speak("Is the product of " + a + " and " + b)


        elif 'change name of a file' in query:
            try:
                speak("Which file on Deskop ?")
                k = str(input("You: "))
                speak("What's the new name")
                d = str(input("You: "))
                f = "C:\\Users\\hp\\Desktop\\" + d 
                g = "C:\\Users\\hp\\Desktop\\" + k
                os.renames(g , f)
                speak("Successfully renamed!")
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'who is ' in query:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speakWithoutSubs(results)
            

        else:
            speak("Sorry sir I am not able to get it! Please repeat what you said")
'''