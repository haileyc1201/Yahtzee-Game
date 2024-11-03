#Importing random for dice rolls
import random

class Die:

  #Initializing die variables
  _d_value = 0
  _d_sides = 0
  
  def __init__(self, sides=6):
    '''Assigns the number of sides from the value passed in. 
    Set value to 0 or to the returned value of roll()'''
    self._d_sides = sides
    self._d_value = self.roll()
    
  def roll(self):
    '''Generate a random number between 1 and the number of sides.
    Assign it to the Die’s value. 
    Return the value.'''
    #Rolls die and returns result
    self._d_value = random.randint(1, self._d_sides)
    return self._d_value
    
  def __str__(self):
    '''returns the die’s value as a string.'''
    return str(self._d_value)
    
  def __lt__(self, other):
    '''Return whether the value of self is less than the value of other.'''
    return (self._d_value < other._d_value)
    
  def __eq__(self, other):
    '''Return whether the value of self is equal to the value of other.'''
    return self._d_value == other._d_value
      
  def __sub__(self, other):
    '''Return the difference between the value of self and the value of other.'''
    return self._d_value - other._d_value