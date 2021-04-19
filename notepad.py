import speech_recognition as sr
import pyttsx3
from pathlib import Path

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


def user_input(speech):
    with sr.Microphone() as source:
        speaker(speech)
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            return text
        except:
            speaker('sorry!! could not recognize your voice.')
            speaker('please repeat')
            try:
                audio = r.listen(source)
                repeated_text = r.recognize_google(audio)
                return repeated_text
            except:
                speaker('voice recognition failed. exiting now...')


action = user_input('what\'s the action?(reading or writing)')
print(action)


action_end = False

while not action_end:
    if action == 'writing':
        file_name = input('Enter your file namme: ')
        speaker('you entered {} as your file name.'.format(file_name))
        if Path(file_name).is_file():
            speaker('File {} already exists'.format(file_name))
            file_action = user_input('Do you want to overwrite or append?')
            print(file_action)
            file_action_end = False
            while not file_action_end:
                if file_action == 'overwrite':
                    fh = open(file_name, 'w')
                    context = user_input('What\'s the context of your file?')
                    fh.write(context)
                    fh.close()
                    print(context)
                    file_action_end = True
                elif file_action == 'append':
                    fh = open(file_name, 'a')
                    context = user_input('What\'s the context of your file?')
                    fh.write(context)
                    fh.close()
                    print(context)
                    file_action_end = True
                else:
                    file_action = user_input(
                        'Unrecognized file action. please repeat.. \nDo you want to overwrite or append?')
        else:
            speaker('File {} doesn\'t exist. creating a new one..'.format(file_name))
            fh = open(file_name, 'w')
            context = user_input('What\'s the context of your file?')
            fh.write(context)
            fh.close()
            print(context)
        action_end = True
    elif action == 'reading':
        file_name = input('Enter your file namme: ')
        speaker('you entered {} as your file name.'.format(file_name))
        if Path(file_name).is_file():
            speaker('file {} exists.'.format(file_name))
            fh = open(file_name, 'r')
            context = fh.read()
            speaker(context)
            action_end = True
        else:
            action = user_input(
                'file {} doesen\'t exist. Try writing instead of reading. \nWhat\'s the action?(reading or writing)'.format(file_name))
            print(action)
    else:
        action = user_input(
            'invalid action type. try reading or writing. \nWhat\'s the action?(reading or writing)')
        print(action)
