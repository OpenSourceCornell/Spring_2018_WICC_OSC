#you have a vendetta against Apple.  Return the inputted list, with
#every element that contains the substring 'apple' removed.
#ex: ['apple', 'Apple', 'I<3apple', 'banana', 'Microsoft']
#return: ['Apple', 'banana', 'Microsoft']
def no_apples(input_list):
  new = []
  print("here")
	for item in input_list:
    lower_item = item.lower()
    if "apple" not in lower_item:
      new += [item]
  return new