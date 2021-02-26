

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%H:%M:%S")

from datetime import date

today = date.today()
d2 = today.strftime("%B %d, %Y")



import speech_recognition
import pyttsx3
while True:
    robot_ear=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        audio = robot_ear.listen(mic)

    try:
        you=robot_ear.recognize_google(audio)
    except:
        you = ""
    print(you)
    if you == "":
        robot_brain=""
    elif you == "hello":
        robot_brain="hello chinh"
    elif "today" in you:
        robot_brain=d2
    elif "time" in you:
        robot_brain=dt_string
    elif "i am" in you:
        robot_brain="what is your name"
    elif "bye" in you:
        robot_brain="bye chinh"
        engine = pyttsx3.init()
        engine.say(robot_brain)
        engine.runAndWait()
        break
    elif "name" in you:
        robot_brain="i am robot con hihi"

    else:
        robot_brain=""
    engine = pyttsx3.init()
    engine.say(robot_brain)
    engine.runAndWait()
    