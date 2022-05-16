# The import random function is a built in module of Python used to generate a random value.
import random
print('This is a random suit generator.')

# Sets the seven options for jacket colors.
jackets = ('Black', 'Navy', 'Brown','Gray', 'Tan')

# Creates a new variable that randomly selects one of the seven jacket colors.
# The random.choice method returns a randomly selected part from a specific sequence.
jacket = random.choice(jackets)

# Outputs a combination of strings and sequence to display "Wear a (random jacket color) dress shirt."
print('Wear a ' + jacket + ' jacket.')

dressShirt = ('White', 'Cream', 'Powder Blue')
dresshirt = random.choice(dressShirt)
print('With a ' + dresshirt + ' dress shirt')

pants = ('Black', 'Navy', 'Brown', 'Gray', 'Tan')
pant = random.choice(pants)
print('and ' + pant + ' pants.')

print('The ' + jacket + ' jacket with a ' + dresshirt + ' shirt and ' + pant + ' pants will look nice!')

print('******** Now you have sharp outfit! ********')
print('Enjoy')