#Importing die class
import die

class Player:
  
  #Initializing local variables
  _points = 0
  _dice = []
  
  def __init__(self):
    '''Constructs and sorts the list of three Die objects
    Initializes the player’s points to 0'''
    self._dice = [die.Die(), die.Die(), die.Die()]
    self._points = 0
    
  def get_points(self):
    '''Returns the player’s points.'''
    return self._points
    
  def roll_dice(self): 
    '''Calls roll on each of the Die objects in the dice list
    Sorts the list.'''
    
    #Rolling dice
    for dice in self._dice:
      dice.roll()
      
    #Sorting dice
    self._dice.sort()
    
  def has_pair(self):  
    '''Returns true if two dice in the list have the same value (uses ==). 
    Increments points by 1.'''

    #Checking for a matching pair
    if (self._dice[0] == self._dice[1]
        or self._dice[1] == self._dice[2]):

      #Incrementing points
      self._points += 1
      return True

    #If no pair is found, return false
    else:
      return False
  
  def has_three_of_a_kind(self):
    '''Returns true if all three dice in the list have the same value (uses ==). 
    Increments points by 3.'''
    
    #Checking if all dice rolls are equal
    if (self._dice[0] == self._dice[1] == self._dice[2]):
      self._points += 3
      return True 

    #If not, returns false
    else:
      return False
  
  def has_series(self):
    '''Returns true if the values of each of the dice in the list are in sequence
    Ex: 1,2,3 or 2,3,4 or 3,4,5 or 4,5,6) (uses -). 
    Increments points by 2.'''
    #Checks for sequence 
    if (self._dice[0] - self._dice[1] == -1 and self._dice[1] - self._dice[2] == -1):
      #Adds points if true and returns true
      self._points += 2
      return True
    #If not sequence, returns false 
    else:
      return False
    
  def __str__(self):
    '''Returns a string in the format: “D1=2, D2=4, D3=6”.'''
    #Creates a string variable 
    s = ""
    #Puts each dice in list into string variable as format D1=1 then returns
    for i in range(len(self._dice)):
      s += "D" + str(i) + "=" + str(self._dice[i]) + " "
    return s
