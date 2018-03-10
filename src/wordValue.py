#given a dict of letter to numeric value mappings, calculate the value of the given word
#example valueDict = {'o': 3, 's': 7} word = 'os'
#return 3+7 = 10
def word_value(valueDict, word):
  value = 0
  for i in word:
    value += valueDict[str(i)]
  return value
