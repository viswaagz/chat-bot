import re 
import long as king

def message_prob(user_message, regonised_words, single_responce=False, required_words=[]):
    message_certainty=0
    has_reqired_words = True

    for word in user_message:
     if word in regonised_words:
        message_certainty += 1

    percentage= float(message_certainty)/float(len(regonised_words))

    for word in required_words:
        if word not in user_message:
            has_reqired_words=False
            break
    
    if has_reqired_words or single_responce:
        return int(percentage*100)
    else:
        return 0 

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, List_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response]= message_prob(message, List_of_words, single_response, required_words) 

    #response
    response('hello!',['hello','hii','sup','hey'], single_response=True)
    response('I\'m doing fine, and you',['how','are','you','doing'],required_words=['how'] )

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)

    return best_match



def get_response(user_input):
    split_message = re.split(r'\s+| [,;?.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# testing the responce
while True:
    print('Virtual assistant : ' + get_response(input('You: ')))
