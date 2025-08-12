import pyttsx3
engine = pyttsx3.init()

print("Welcome To Robot Speaker 1.0")
engine.say("Welcome To Robot Speaker 1.0")
engine.runAndWait()


engine.say("What you want to Speak")
engine.runAndWait()

while True:
    saying=input("What you want to Speak ")
    if saying=='|':
        break
    engine.say(saying)
    engine.runAndWait()

