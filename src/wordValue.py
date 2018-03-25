#given a dict of letter to numeric value mappings, calculate the value of the given word
#example valueDict = {'o': 3, 's': 7} word = 'os'
#return 3+7 = 10
def word_value(valueDict, word):
    wordlist=[x for x in word if word!=' ']
    sum=0
    for k in [valueDict[j] for i in wordlist for j in valueDict.keys() if i==j]: sum+=k
    return sum
