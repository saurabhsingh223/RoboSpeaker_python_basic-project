import pyttsx3

engine = pyttsx3.init()

while(True):
    x = input("Enter what you want to speak ( or type 'bye, to quit): ")
    if x.lower() == 'bye':
        engine.say("Goodbye friend")
        engine.runAndWait()
        break
    engine = pyttsx3.init()
    engine.say(x)
    engine.runAndWait()



