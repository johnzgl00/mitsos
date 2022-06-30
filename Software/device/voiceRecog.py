import speech_recognition as sr

def main():
    r = sr.Recognizer

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say Shit")
        audio = r.listen(source)
        
        try:
            print("You Said: " + r.recognize_google(audio))
        
        except Exception as e:
            print("Error: " + str(e))

main()