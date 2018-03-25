# As a firm Silicon Valley fanatic, you have been
# inspired by Jian Yang's hot dog/not hot dog classifier,
# and decided to build your own classifier... but for text!
# Your objective is to take a body of text, and two word inputs, and return a score count.
# Every time the first string occurs in the text, you will
# increment the score count, and every time the second string
# occurs, you will decrement the score count. Return the final score.
# Example: 
# input: ("I love to eat hot dogs for breakfast, hot dogs for lunch, and even for dinner!", "hot", "for")
# output: -1

def text_score(message, positive_word, negative_word):
    message_list=message.split()
    Score_Count=0
    for i in message_list:
        if i==positive_word: Score_Count+=1
        elif i==negative_word: Score_Count-=1
    return Score_Count
