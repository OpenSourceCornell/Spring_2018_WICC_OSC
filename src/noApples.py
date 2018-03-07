#you have a vendetta against Apple.  Return the inputted list, with
#every element that contains the substring 'apple' removed.
#ex: ['apple', 'Apple', 'I<3apple', 'banana', 'Microsoft']
#return: ['Apple', 'banana', 'Microsoft']
def no_apples(input_list):
  new = []
  for item in input_list:
    if "apple" not in item:
      new += [item]
  return new