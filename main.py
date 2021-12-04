import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import sqlite3 as db
import random as rd


ateambot = ChatBot(name='Sabot',
                   read_only=True,
                   storage_adapter='chatterbot.storage.SQLStorageAdapter',
                   logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch',
                                    'maximum_similarity_threshold': 0.90,
                                   'default_response': 'sorry was not able to generate a response for you'}],
                   databaseuri='sqlite3:///database.sqlite3',
                   )

trainer = ListTrainer(ateambot)


def train_data():
    trainer_array = []
    with open('possible responses', 'r') as file:
        intents = json.load(file)
    for data in intents["intents"]:
        for intent in data['patterns']:
            trainer_array.append(intent)
            trainer_array.append(rd.choice(data['responses']))
            trainer.train(trainer_array)
            trainer_array.clear()


def database_writer(table, record):
    print(record)
    database_connector = db.connect('db.sqlite3')
    cursor = database_connector.cursor()
    if table == 'tag':
        sql_query = f'INSERT INTO {table}(name) VALUES (?)'
        cursor.execute(sql_query, (record,))
        database_connector.commit()
        database_connector.close()


def tag_checker(tag):
    database_connector = db.connect('db.sqlite3')
    cursor = database_connector.cursor()
    sql_query = 'SELECT (name) FROM tag ;'
    tags = list(cursor.execute(sql_query))
    for tagg in tags:
        if tag == tagg[0]:
            database_connector.close()
            return True
        else:
            print('tag not reading')
            database_connector.close()
    return False


def json_file_reader():
    with open('possible responses', 'r') as file:
        intents = json.load(file)
    for data in intents["intents"]:
        if tag_checker(data['tag']):
            pass
        else:
            database_writer('tag', data['tag'])


def update_statement_id():
    pass


def program_start():
    text = True
    positive_checker: bool = False
    train_data()
    json_file_reader()
    name = input('What is your name?')
    print('SUIBOT: Welcome to southampton solent university interactive bot')
    response = input('''which of the following ways would you rather communicate with me
    [1]Text
    [2]Voice
    [0]Exit
    Answer: ''')
    if response == '1':
       text_function(name)
    elif response == '2':
        text = False
    elif response == '0':
        print('Thank you for stopping by exiting now')
        exit(0)
    else:
        print('invalid selection, text has been automatically chosen for you')
    name = input('hello, what is your name?')
    while True:
        intent = input(name+' how can i help you?')
        if intent.__contains__('exit'):
            print('thanks for stopping by')
            break
        else:
            ateambot.get_response(intent)
            positive_checker_string = input('was that helpful?:')
            if positive_checker_string.__contains__('yes') or positive_checker_string.__contains__('yeah'):
                ateambot.learn_response()
            else:
                positive_checker = False


def text_function(name):
    while True:
        question = input(f'SUIBOT: hello {name} how can i help you?')
        print(f'suibot: {ateambot.get_response(question)}')
        feedback = input('Did that help?')
        if feedback == 'Yes':
            break
        else:
            continue


def voice_function():
    pass


program_start()

