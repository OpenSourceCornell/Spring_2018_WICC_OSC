#!/usr/bin/python3

from recipe import recipe

# A cookie recipe
# Possible Modifications:
# 	changes in ingredients
# 	changes in directions
# 	create a new recipe file

cheesecake_ingredients = {
	'HONEY MAID Graham Cracker Crumbs' : '1 3/4 cups ',
	'butter, melted' : '1/3 cup',
	'sugar, divided' : '1 1/4 cups',
	'packages PHILADELPHIA Cream Cheese, softened' : '3 (8 ounce)',
	'BREAKSTONE\'S or KNUDSEN Sour Cream' : '1 cup',
	'vanilla' : '2 teaspoons',
	'eggs' : '3 ',
	'can cherry pie filling' : '1 (21 ounce)'
}

cheesecake_directions = [
	'Heat oven to 350 degrees F.',
	'Mix graham crumbs, butter and 1/4 cup sugar; press onto bottom of 9-inch springform pan.',
	'Beat cream cheese and remaining sugar in large bowl with mixer until blended. Add sour cream and vanilla; mix well. Add eggs, 1 at a time, beating on low speed after each addition just until blended. Pour over crust.',
	'Bake 1 hour to 1 hour 10 min. or until center is almost set. Run knife around rim of pan to loosen cake; cool before removing rim. Refrigerate cheesecake 4 hours.',
	'Top with pie filling before serving.'
]

cheesecake_recipe = recipe(cheesecake_ingredients, cheesecake_directions)
cheesecake_recipe.print_ingredients()
cheesecake_recipe.print_directions()

