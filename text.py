from chatterbot.conversation import Statement


def text_func(chatbot):
    name = input('SUIBOT: hello, what is your name?: ')
    print(name + 'welcome to solent university interactive bot(type exit to stop anytime)')
    while True:
        print('how can i help you?')
        intent = input(name + ':').lower()
        if intent.__contains__('exit'):
            print('thanks for stopping by')
            break
        else:
            intention = chatbot.get_response(intent)
            print('SABOT ', intention)
            positive_checker_string = input('was that helpful?:').lower()
            if yes_checker(positive_checker_string):
                break
            else:
                if positive_checker_string.__contains__('exit'):
                    break
                else:
                    print('you can help with my learning process, reply with a yes if you wish to help')
                    if yes_checker(input(name + ':')):
                        while True:
                            print('SABOT: ok give the answer to your question')
                            answer_text = input(name + ':')
                            answer = input('SABOT:are you satisfied with your answer?:')
                            if yes_checker(answer):
                                statement = Statement(answer_text)
                                statement.confidence = 1.0
                                statement.in_response_to = intent
                                chatbot.learn_response(statement, intent)
                                chatbot.read_only = True
                                break
                            elif answer.__contains__('exit') or answer.__contains__('quit'):
                                break
                            elif answer.__contains__('no') or answer.__contains__('not really'):
                                continue
                            else:
                                break
                    if yes_checker(input('SABOT: anything else?: ')):
                        continue
                    else:
                        print('SABOT: thank you for engaging, hope you come back soon')
                        break


def yes_checker(sentence):
    if sentence.__contains__('yeah') or sentence.__contains__('yes'):
        return True
    else:
        return False
