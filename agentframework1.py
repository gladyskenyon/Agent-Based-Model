# Import library to generate random numbers
import random 


# Create a class of Agent
class Agent:
    # Constructor of Agent 
    def __init__ (self, environment, agents, neighbourhood): # Passes in varibale lists to link to objects
        
        self.environment = environment # Used in eat method as grass for sheep
        self.store = 0 # Creates a store of food for each agent in eat and sick methods
        self.agents = agents # Used in share with neighbours method
       
        self._x = random.randint(0,100) # Set starting x co-ordinates randomly in the field between 0 and 100
        self._y = random.randint(0,100) # Set starting y co-ordinates randomly between 0 and 100
        
              
    # Protect x and y using get and set methods
    def getx(self): # Take self into getx
        return self._x # Return with an underscore, acts as a password

    def gety(self):
        return self._y # Do same for y
    
    def setx(self, value):
        self._x = value
    
    def sety(self, value):
        self._y = value
        


    # Create method for sheep to move - use a torus o stop sheep wandering off the field   
    def move(self): # Take in self argument
        
        if random.random() < 0.5: # If random number is less than 0.5
            self._x = (self._x + 1) % 100 # Add 1 to x co-ordinate of sheep 
        else:                             # If random number is more than 0.5
            self._x = (self._x - 1) % 100 # Minus 1 from x co-ordinate of sheep
        
        if random.random() < 0.5:         # # If random number is less than 0.5
            self._y = (self._y + 1) % 100 # Add 1 to y co-ordinate of sheep
        else:                             # # If random number is more than 0.5
            self._y = (self._y - 1) % 100 # Minus 1 from y co-ordinate of sheep



    # Create method to make sheep eat the grass and store it in their stomachs
    def eat(self): # Take in self argument
        
        if self.environment[self._y][self._x] > 10: # If the environment (field) is more than 10            
            self.environment[self._y][self._x] -= 10 # Minus 10 from the field            
            self.store += 10 # Add 10 to the sheeps store (stomach)
    
    
    
    # Create sick method, take in self argument
    def sick(self):
        
        if self.store >= 100: # If sheep eat more than 100 grass
            if self.store + self.environment[self._y][self._x] <250: # if self plus eviroment store is less than 250
                self.environment[self._y][self._x] += (self.store) # Store goes back into environment
                self.store = 0 # Reset agent store to 0
            else: 
                self.environment [self._y] [self._x] += (250 - self.environment [self._y] [self._x])
                self.store -= (250 - self.store)
                
    
    # Create method for sheep to share grass with others    
    def share_with_neighbours(self, neighbourhood): # Take in self and neighbourhood arguments
            
        for agent in self.agents: # For each sheep           
            dist = self.distance_between(agent) # Make variable for distance between two sheep
            if dist <= neighbourhood: # If sheep are in each others neighbourhod, as defined in model.py
                
                sum = self.store + agent.store # Sum the two sheeps food stores
                ave = sum /2 # Divide sum by 2 to get an average 
                self.store = ave # Give the sheep the average grass store
                agent.store = ave # Give the sheep the average grass store
       
                
       
    # Define distance between method to work out distance between 2 sheep
    def distance_between(self, agent): # Take in self and other sheep
        return (((self._x- agent._x)**2) + ((self._y- agent._y)**2))**0.5  # Pythagprus theorum   
        