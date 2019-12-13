#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = []
  #iterate over the keys of the recipe
  for ingredient in recipe:
    #check if the ingredient exists in ingredients
    if ingredient in ingredients:
      #check if the amount needed for the recipe is less than or equal the amount of that ingredient we have.
      if recipe[ingredient] <= ingredients[ingredient]:
        #generate the number of batches we can make for this ingredient alone 
        batch_count = ingredients[ingredient] // recipe[ingredient]
        #append the batch_count to batches list 
        batches.append(batch_count)
      else:
        #this condition hits when we don't have enough ingredients to make a batch 
        return 0
    else:
      #this condition hits when we don't have the ingredient in the recipe dictionary in the ingredients dictionary. 
      return 0
  #end of the for loop 

  #return the minimum number of batches as the answer 
  return min(batches)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))