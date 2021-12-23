import speech_recognition as sr
import pyttsx3
import urllib.request
import urllib.error
import pywintypes
from chatterbot import ChatBot
from chatterbot.conversation import Statement


speech_engine = pyttsx3.init()
speech_engine.setProperty('rate', 145)
r = sr.Recognizer()
voices = speech_engine.getProperty('voices')
speech_engine.setProperty('voice', voices[1].id)


def speech_function(chatbot):
    with sr.Microphone() as source:
        speaker('adjusting for background noise please be quiet')
        r.adjust_for_ambient_noise(source, duration=1)
        speaker('What is your name?')
        name_sound = r.listen(source)
        try:
            if internet_checker():
                name = r.recognize_google(name_sound)
                name = str(name).lower()
                speaker(f'{name} Welcome to southampton solent university interactive bot')
                while True:
                    speaker('how can i help you?')
                    intent_sound = r.listen(source)
                    intent = r.recognize_google(intent_sound)
                    intention = chatbot.get_response(intent)
                    speaker(intention)
                    speaker('was that helpful?')
                    response = r.listen(source)
                    response_text = str(r.recognize_google(response)).lower()
                    if yes_checker(response_text):
                        speaker('thank you for helping my learning process talk later')
                    elif response_text.__contains__('exit') or response_text.__contains__('quit'):
                        break
                    elif response_text.__contains__('no') or response_text.__contains__('not really'):
                        speaker('you can help with my learning process, please reply with a yes if you wish to help')
                        willingness = r.listen(source)
                        willingness_text = str(r.recognize_google(willingness)).lower()
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
                                    break
                                elif answer.__contains__('exit') or answer.__contains__('quit'):
                                    break
                                elif answer.__contains__('no') or answer.__contains__('not really'):
                                    continue
                                else:
                                    break
                        speaker('anything else')
                        if yes_checker(listener(source)):
                            continue
                        else:
                            speaker('thank you for engaging, hope you come back soon')
                            break
                    else:
                        continue
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


if __name__ == '__speech__':
    pass
