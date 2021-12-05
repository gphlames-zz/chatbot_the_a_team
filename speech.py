import speech_recognition as sr
import pyttsx3
import pywintypes


def speech_function(chatbot):
    speech_engine = pyttsx3.init()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speech_engine.say('adjusting for background noise please be quiet')
        r.adjust_for_ambient_noise(source, duration=2)
        speech_engine.say('What is your name?')
        speech_engine.runAndWait()
        name_sound = r.listen(source)
        name = r.recognize_google(name_sound)
        name = str(name).lower()
        speech_engine.say(f'{name} Welcome to southampton solent university interactive bot')
        speech_engine.runAndWait()
        while True:
            speech_engine.say(name + ' how can i help you?')
            speech_engine.runAndWait()
            intent_sound = r.listen(source)
            intent = r.recognize_google(intent_sound)
            speech_engine.say(chatbot.get_response(intent))
            speech_engine.runAndWait()
            speech_engine.say('was that helpful?')
            speech_engine.runAndWait()
            response_sound = r.listen(source)
            response = str(r.recognize_google(response_sound)).lower()
            if response.__contains__('Yeah') or response.__contains__('yes'):
                speech_engine.say('thank you for helping my learning process talk later')
                speech_engine.runAndWait()
                chatbot.learn_response(response)
            elif response.__contains__('exit') or response.__contains__('quit'):
                break
            else:
                continue


if __name__ == '__speech__':
    pass
