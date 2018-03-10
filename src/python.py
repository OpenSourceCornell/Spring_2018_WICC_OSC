# Your friend has become a firm python fanatic,
# to the point where he will only speak in sentences
# that contain all of the letters in the word python
# Your objective is, given a string, return true if
# it contains all the letters p, y, t, h, o, n, and return
# false otherwise

def python(sentence):
    letters = set(sentence)
    word = 'python'
    for c in word:
        if c not in letters:
            return False
    return True
