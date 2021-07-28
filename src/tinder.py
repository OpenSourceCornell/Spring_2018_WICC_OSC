# One of your friends has proposed
# a superior tinder, to aid fellow Cornell
# students on their dating expeditions
# Your objective is, given two lists of
# hobbies for two different people,
# return "like" if one of the hobbies
# match between the two people, "dislike"
# if nothing matches, and "super like"
# if two or more hobbies match

def tinder(qt1, qt2):
    v = set()
    for el in qt1:
        v.add(el)
    
    counter = 0
    for el in qt2:
        if el in v:
            counter += 1

    if counter == 0:
        return 'dislike'

    if counter == 1:
        return 'like'

    if counter > 1:
        return 'super like'
            

