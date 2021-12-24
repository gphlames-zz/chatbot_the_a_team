import speech_recognition
import speech_recognition as sr
import pyttsx3
import urllib.request
import urllib.error
import pywintypes
from chatterbot.conversation import Statement
import matplotlib.image as img
import matplotlib.pyplot as plt


speech_engine = pyttsx3.init()
speech_engine.setProperty('rate', 145)
r = sr.Recognizer()
voices = speech_engine.getProperty('voices')
speech_engine.setProperty('voice', voices[1].id)
google_api_key = ''
name_of_bot = 'suibot'


def speech_function(chatbot, trainer):
    with sr.Microphone() as source:
        speaker('my name is' + name_of_bot + 'and i will be speaking with you')
        speaker('adjusting for background noise please be quiet')
        r.adjust_for_ambient_noise(source, duration=1)
        speaker('What is your name?')
        try:
            if internet_checker():
                try:
                    name = listener(source)
                except (speech_recognition.UnknownValueError, speech_recognition.RequestError):
                    speaker('there was an error getting your name i will call you student')
                    speaker('i will call you student')
                if name == '':
                    pass
                else:
                    speaker(f'{name} Welcome to southampton solent university interactive bot')
                    while True:
                        try:
                            speaker('how can i help you?')
                            intent = listener(source)
                            intention = chatbot.get_response(intent)
                            speaker(intention)
                            speaker('was that helpful?')
                            response_text = listener(source)
                            if yes_checker(response_text):
                                image_display(intention)
                                speaker('thank you for helping my learning process talk later')
                            elif response_text.__contains__('exit') or response_text.__contains__(
                                    'quit') or response_text.__contains__('stop'):
                                break
                            elif response_text.__contains__('no') or response_text.__contains__('not really'):
                                speaker(
                                    'you can help with my learning process, please reply with a yes if you wish to help')
                                willingness_text = listener(source)
                                if yes_checker(willingness_text):
                                    while True:
                                        speaker('ok give the answer to your question')
                                        answer_text = listener(source)
                                        speaker(answer_text)
                                        speaker('are you satisfied with your answer?')
                                        answer = listener(source)
                                        if yes_checker(answer):
                                            statement = Statement(answer_text)
                                            statement.confidence = 1.0
                                            statement.in_response_to = intent
                                            chatbot.learn_response(statement, intent)
                                            for _ in range(25):
                                                trainer.train([intent, answer_text])
                                            break
                                        elif answer.__contains__('exit') or answer.__contains__('quit'):
                                            break
                                        elif answer.__contains__('no') or answer.__contains__('not really'):
                                            continue
                                        else:
                                            break
                            else:
                                continue
                        except(speech_recognition.UnknownValueError, speech_recognition.RequestError):
                            speaker('there was an error with your query please try again')
                            continue
                        speaker('anything else')
                        if yes_checker(listener(source)):
                            continue
                        else:
                            speaker('thank you for engaging, hope you come back soon')
                            break
            else:
                speaker('you do not have an active internet connection please try again')
        except urllib.error.URLError:
            speaker('you do not have an active internet connection please try again')


def speaker(sentence):
    speech_engine.say(sentence)
    speech_engine.runAndWait()


def yes_checker(sentence):
    if sentence.__contains__('yeah') or sentence.__contains__('yes'):
        return True
    else:
        return False


def internet_checker():
    try:
        urllib.request.urlopen('https://www.google.com/', timeout=1)
        return True
    except urllib.error.URLError as err:
        return False


def listener(source):
    answer = r.listen(source)
    answer_text = str(r.recognize_google(answer)).lower()
    return answer_text


def image_display(reply):
    list_of_images = ['gym', 'library', 'micheal andrews', 'solent shop', 'spark building', 'student hub', 'student kitchen']
    for name in list_of_images:
        if name in reply:
            place = img.imread('/images/' + name)
            plt.imshow(place)
            plt.show()


if __name__ == '__speech__':
    pass
