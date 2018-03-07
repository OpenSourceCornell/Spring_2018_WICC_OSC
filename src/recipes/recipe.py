#!/usr/bin/python3

# Represents a recipe
# 
# Possible Modifications:
# 	change the way ingredients are printed
# 	change the way directions are printed

class recipe():

	def __init__(self, ingredients, directions):
		self.ingredients = ingredients
		self.directions = directions
	
	def print_ingredients(self):
		print('Ingredients:')
		for key, value in self.ingredients.items():
			print(key + ' - ' + value)
		print('\n')

	def print_directions(self):
		print('Directions:')
		for step in self.directions:
			print(step)
		print('\n')