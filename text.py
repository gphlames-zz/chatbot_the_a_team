from chatterbot.conversation import Statement
from PIL import Image as img

name_of_bot = 'SUIBOT: '


def text_func(chatbot, trainer):
    name = input(name_of_bot + 'hello, what is your name?: ')
    print(name_of_bot + name + ' welcome to solent university interactive bot(type exit to stop anytime)')
    while True:
        print(name_of_bot + 'how can i help you?')
        intent = input(name + ':').lower()
        if intent.__contains__('exit'):
            print('thanks for stopping by')
            break
        else:
            intention = chatbot.get_response(intent)
            print(name_of_bot + intention.text)
            print(name_of_bot + 'was that helpful?')
            positive_checker_string = input(name + ':').lower()
            if yes_checker(positive_checker_string):
                image_display(intention)
                break
            else:
                if positive_checker_string.__contains__('exit'):
                    break
                else:
                    print(name_of_bot + 'you can help with my learning process, reply with a yes if you wish to help')
                    if yes_checker(input(name + ':')):
                        while True:
                            print(name_of_bot + 'ok give the answer to your question')
                            answer_text = input(name + ':')
                            answer = input(name_of_bot + 'are you satisfied with your answer?:')
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
                    if yes_checker(input(name_of_bot + 'anything else?: ')):
                        continue
                    else:
                        print(name_of_bot + 'thank you for engaging, hope you come back soon')
                        break


def image_display(reply):
    list_of_images = ['gym', 'library', 'micheal andrews', 'solent shop', 'spark building', 'student hub', 'student kitchen']
    for name in list_of_images:
        if name in reply.text:
            try:
                image = img.open(f'images/' + f"{name}" + '.jpg')
                image.show()
            except (FileNotFoundError,):
                print('failed to locate image to display your destination')


def yes_checker(sentence):
    if sentence.__contains__('yeah') or sentence.__contains__('yes'):
        return True
    else:
        return False
