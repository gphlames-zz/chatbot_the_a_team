import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import random as rd
import text
import speech
import speech_recognition as sr


ateambot = ChatBot(name='simi',
                   storage_adapter='chatterbot.storage.SQLStorageAdapter',
                   logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch',
                                    'maximum_similarity_threshold': 0.85,
                                   'default_response': 'sorry was not able to generate a response for you, please visit the student hub.'}],
                   databaseuri='sqlite3:///database.sqlite3',
                   )
trainer = ListTrainer(ateambot)
trainer.show_training_progress = False
name_of_bot = 'simi'


def train_data():
    trainer_array = []
    with open('possible responses', 'r') as file:
        intents = json.load(file)
    for data in intents["intents"]:
        if 'patterns' in data:
            for intent in data['patterns']:
                trainer_array.append(intent)
                trainer_array.append(rd.choice(data['responses']))
                trainer.train(trainer_array)
                trainer_array.clear()
        if 'conversations' in data:
            trainer.train(data['conversations'])


def program_start():
    train_data()
    speech.speaker('hello my name is' + name_of_bot + ',Welcome to southampton solent university interactive bot')
    activity_string = '''select the following way you would prefer to communicate with me,
       [1] for Text,
       [2] for Verbal communication,
       [0] to Exit,
       Answer: '''
    speech.speaker(activity_string)
    with sr.Microphone() as source:
        response = speech.listener(source)
        if response.__contains__('1') or response.__contains__('text'):
            text.text_func(ateambot, trainer)
        elif response.__contains__('2') or response.__contains__('verbal'):
            speech.speech_function(ateambot, trainer)
        elif response.__contains__('0') or response.__contains__('exit'):
            speech.speaker('Thank you for stopping by exiting now')
            exit(0)
        else:
            print('invalid selection, text has been automatically chosen for you')
            text.text_func(ateambot, trainer)


program_start()

