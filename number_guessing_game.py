import speech_recognition as sr
import pyttsx3
import random

game_over = False

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 125)
r = sr.Recognizer()
r.dynamic_energy_threshold = False


def speaker(speech):
    print(speech)
    engine.say(speech)
    engine.runAndWait()


winning_number = random.randint(1, 100)
# print(winning_number)
guess = 1

# Getting the input
with sr.Microphone() as source:
    speaker('Enter a number: ')
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        number = int(text)
        print(number)
    except:
        speaker('sorry!! could not recognize your voice.')

# building the game
    while not game_over:
        try:
            if number == winning_number:
                speaker('You win!! you guessed this number in {} time'.format(guess))
                game_over = True
            else:
                if number < winning_number and number >= 0:
                    speaker('You guessed a lower number')
                    guess += 1
                    speaker('Guess again: ')

                elif number > winning_number:
                    speaker('You guessed a higher number')
                    guess += 1
                    speaker('Guess again: ')
                else:
                    speaker('You guessed a negative number')
                    guess += 1
                    speaker('Guess again: ')
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio)
                        number = int(text)
                        print(number)
                    except:
                        speaker('sorry!! could not recognize your voice.')
        except:
            speaker('sorry!! could not recognize your voice.')
            speaker('Guess again: ')
            with sr.Microphone() as source:
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    number = int(text)
                    print(number)
                except:
                    speaker('sorry!! could not recognize your voice.')
