import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning!')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

    speak('I am python sir, Please tell me how may I help you')


def takeCommand():
    '''it takes microphone input from user and returs sting output to user'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')
    except Exception as e:
        # print(e)
        print('Say that again please...')
        return 'none'
    return query


if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=4)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open whatsapp' in query:
            webbrowser.open('web.whatsapp.com')

        elif 'play music' in query:
            music_dir = r"C:\Users\Vikas\Music\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif ' the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'sir the time is {strTime}')

        elif 'open code' in query:
            codepath = r"C:\Users\Vikas\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)

        elif 'exit' in query:
            exit()