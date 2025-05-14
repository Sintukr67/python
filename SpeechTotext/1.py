#pip install SpeechRecognition
#pip install pyaudio
# Import the necessary libraries

import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Use microphone as source
with sr.Microphone() as source:
    print("Say something...")
    r.adjust_for_ambient_noise(source)  # Optional: helps with noise
    audio = r.listen(source)

    try:
        # Recognize speech using Google Web Speech API
        text = r.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
