import speech_recognition as sr
import pyttsx3
import pywintypes
from chatterbot import ChatBot
speech_engine = pyttsx3.init()
speech_engine.setProperty('rate', 140)
r = sr.Recognizer()
voices = speech_engine.getProperty('voices')
speech_engine.setProperty('voice', voices[1].id)


def speech_function(chatbot):
    #chatbot = ChatBot(chatBot)
    with sr.Microphone() as source:
        speaker('adjusting for background noise please be quiet')
        r.adjust_for_ambient_noise(source, duration=2)
        speaker('What is your name?')
        name_sound = r.listen(source)
        name = r.recognize_google(name_sound)
        name = str(name).lower()
        speaker(f'{name} Welcome to southampton solent university interactive bot')
        while True:
            speaker('how can i help you?')
            intent_sound = r.listen(source)
            intent = r.recognize_google(intent_sound)
            speaker(chatbot.get_response(intent))
            speaker('was that helpful?')
            response = listener(source)
            if yes_checker(response):
                speaker('thank you for helping my learning process talk later')
            elif response.__contains__('exit') or response.__contains__('quit'):
                break
            elif response.__contains__('no') or response.__contains__('not really'):
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
                            chatbot.learn_response(answer_text, intent)
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


def speaker(sentence):
    speech_engine.say(sentence)
    speech_engine.runAndWait()


def yes_checker(sentence):
    if sentence.__contains__('yeah') or sentence.__contains__('yes'):
        return True
    else:
        return False


def listener(source):
    answer = r.listen(source)
    answer_text = str(r.recognize_google(answer)).lower()
    return answer_text




if __name__ == '__speech__':
    pass
