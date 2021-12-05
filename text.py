

def text_func(chatbot):
    name = input('SUIBOT: hello, what is your name?: ')
    while True:
        intent = input(name + ' how can i help you?')
        if intent.__contains__('exit'):
            print('thanks for stopping by')
            break
        else:
            chatbot.get_response(intent)
            positive_checker_string = input('was that helpful?:')
            if positive_checker_string.__contains__('yes') or positive_checker_string.__contains__('yeah'):
                chatbot.learn_response()
            else:
                continue