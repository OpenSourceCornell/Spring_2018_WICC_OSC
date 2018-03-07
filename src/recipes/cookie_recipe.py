#!/usr/bin/python3

from recipe import recipe

# A cookie recipe
# Possible Modifications:
# 	changes in ingredients
# 	changes in directions
# 	create a new recipe file

cookie_ingredients = {
	'butter, softened' : '1 cup',
	'white sugar' : '1 cup',
	'packed brown sugar' : '1 cup',
	'eggs' : '2',
	'vanilla extract' : '2 teaspoons',
	'all-purpose flour' : '3 cups',
	'baking soda' : '1 teaspoon',
	'hot water' : '2 teaspoons',
	'salt' : '0.5 teaspoon',
	'semisweet chocolate chips' : '2 cups',
	'chopped walnuts' : '1 cup'
}

cookie_directions = [
	'Preheat oven to 350 degrees F (175 degrees C).',
	'Cream together the butter, white sugar, and brown sugar until smooth. Beat in the eggs one at a time, then stir in the vanilla. Dissolve baking soda in hot water. Add to batter along with salt. Stir in flour, chocolate chips, and nuts. Drop by large spoonfuls onto ungreased pans.',
	'Bake for about 10 minutes in the preheated oven, or until edges are nicely browned.'
]

cookie_recipe = recipe(cookie_ingredients, cookie_directions)
cookie_recipe.print_ingredients()
cookie_recipe.print_directions()

