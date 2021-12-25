from chatterbot.conversation import Statement
from PIL import Image as img

name_of_bot = 'SUIBOT: '

intents = ''
def text_func(chatbot, trainer):
    name = input(name_of_bot + 'hello, what is your name?: ')
    print(name_of_bot + name + ' welcome to solent university interactive bot(type exit to stop and 1 to teach me anytime)')
    while True:
        intent = input(name + ':').lower()
        intention = None
        if intent == '1':
            pass
        else:
            global intents
            intents = ''
            intents = intents.join(intent)
            intention = chatbot.get_response(intent)
            print(name_of_bot + intention.text)
            image_display(intention)
        if intent.__contains__('exit'):
            print('thanks for stopping by')
            break
        elif intent == '1':
            print(name_of_bot + 'you can help with my learning process, reply with a yes if you wish to help')
            yes_answer = input(name + ':')
            if yes_checker(yes_answer):
                while True:
                    print(name_of_bot + 'ok give the answer to your question')
                    answer_text = input(name + ':')
                    answer = input(name_of_bot + 'are you satisfied with your answer?:')
                    if yes_checker(answer):
                        statement = Statement(answer_text)
                        statement.in_response_to = intents
                        chatbot.learn_response(statement, intents)
                        for _ in range(25):
                            trainer.train([intents, answer_text])
                        break
                    elif answer.__contains__('exit') or answer.__contains__('quit'):
                        break
                    elif answer.__contains__('no') or answer.__contains__('not really'):
                        continue
                    else:
                        break
            elif yes_answer.__contains__('no'):
                print(name_of_bot + 'ok anything else')
            elif yes_answer.__contains__('exit'):
                print(name_of_bot + 'Good bye')
            else:
                continue
        else:
            continue



def image_display(reply):
    list_of_images = ['gym', 'library', 'micheal andrews', 'solent shop', 'spark building', 'student hub', 'student kitchen']
    for name in list_of_images:
        if name in reply.text:
            try:
                image = img.open(f'images/' + f"{name}" + '.jpg')
                image.show()
            except (FileNotFoundError,):
                print('failed to locate image to display your destination')
                continue


def yes_checker(sentence):
    if sentence.__contains__('yeah') or sentence.__contains__('yes'):
        return True
    else:
        return False
