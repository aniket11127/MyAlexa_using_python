import speech_recognition as sr  # Importing the speech recognition library
import pyttsx3  # Importing the text-to-speech conversion library
import pywhatkit  # Importing the pywhatkit library for playing YouTube videos

listener = sr.Recognizer()  # Creating a speech recognition object
engine = pyttsx3.init()  # Initializing the text-to-speech engine
voices = engine.getProperty('voices')  # Getting the list of available voices
engine.setProperty('voice', voices[1].id)  # Setting the voice to the second option

def talk(text):  # Defining a function to convert text to speech
    engine.say(text)  # Converting the text to speech
    engine.runAndWait()  # Waiting for the speech to finish

def take_command():  # Defining a function to take voice commands
    try:
        with sr.Microphone() as source:  # Using the microphone as the audio source
            print('listening...')  # Indicating that the program is listening
            voice = listener.listen(source)  # Listening to the audio input
            command = listener.recognize_google(voice)  # Recognizing the speech using Google's API
            command = command.lower()  # Converting the command to lowercase
            if 'alexa' in command:  # Checking if the command is for Alexa
                command = command.replace('alexa', '')  # Removing the 'alexa' keyword
                print(command)  # Printing the command
    except:  # Catching any exceptions that may occur
        pass
    return command  # Returning the command

def run_alexa():  # Defining a function to run Alexa
    command = take_command()  # Taking a voice command
    print(command)  # Printing the command
    if 'play' in command:  # Checking if the command is to play a song
        song = command.replace('play', '')  # Extracting the song name
        talk('playing '+ song)  # Announcing the song
        pywhatkit.playonyt(song)  # Playing the song on YouTube
    else:
        talk('Please say the command again.')  # Asking the user to repeat the command
        while True:  # Entering an infinite loop to continue taking commands
            run_alexa()  

run_alexa()  # Running Alexa