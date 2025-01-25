import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import webbrowser

r = sr.Recognizer()

def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening for your command...")
            audioin = r.listen(source)

            my_text = r.recognize_google(audioin)
            my_text = my_text.lower()
            print("You said:", my_text)

            if "open calendar" in my_text:
                speak("Opening calendar for you.")
                # This opens the calendar app on the system
                webbrowser.open('https://www.google.com/calendar')  # This opens Google Calendar in a web browser

            elif "what time is it" in my_text:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The current time is {current_time}.")

            else:
                speak("Sorry, I didn't understand that. Please try again.")

    except Exception as e:
        print("Error occurred:", e)
        speak("Sorry, there was an error. Please try again.")

# Start the assistant
speak("Hi Mrigaank, how are you? How can I help you?")
commands()
