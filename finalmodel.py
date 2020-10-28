# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:55:21 2020

@author: sggkenyo
"""




# IMPORT LIBRARIES
import random # For random number generation
import matplotlib.pyplot as plt # For plotting, use shorthand 
from matplotlib.animation import FuncAnimation # For animation
import tkinter # For GUI programming
import csv # For reading in csv files
import agentframework1 # Contains the Agent class
import matplotlib # For mapping 
matplotlib.use('TkAgg') # For creating GUI


# CREATE THE ENVIRONMENT - FIELD FOR SHEEP
# Create environment 
# Use CSV reader code to read in text file
f = open('in.txt', newline = '')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
# Create empty environment list
environment = []


# Shift environment into a 2.D. list
for line in reader:	
    rowlist = []
# Attach every value to rowlist
    for value in line:
        rowlist.append(value)
# Attach rowlist to environment
    environment.append(rowlist)
#print(environment)
    

# SET CHANGABLE VARIABLES   
# For the number of sheep (agents)
num_of_agents = 50

# For the number of times the model runs
num_of_iterations = 50

# For the proximity of sheep to share resources with others
neighbourhood = 40



# CREATE THE AGENTS - SHEEP TO GRAZE FIELD
# Create empty list for agents
agents = []

# Give each agent access to info on others
for i in range(num_of_agents):
    agents.append(agentframework1.Agent(environment, agents, neighbourhood))


# Check the agentframework file is connected using print
a = agentframework1.Agent(environment, agents, neighbourhood)
print(a._y, a._x)
# Check the co-ordinates move
a.move()
print(a._y, a._x)

# Activate agents
for j in range(num_of_iterations):
    # Use this to reorganise list of agents
    random.shuffle(agents)    
    # For each agent initialize behaviour        
    for i in range(num_of_agents):
                
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours
        agents[i].sick()

        
        

# ANIMATE THE MODEL
# Create update function
def update(frame_number):
    
    # Clear figure
    plt.clf()
             
    for i in range(num_of_agents):
        
            if random.random() < 0.5:                
                agents[i]._x  = (agents[i]._x + 1) % 300                
            else:        
                agents[i]._x  = (agents[i]._x - 1) % 300
                
            
            if random.random() < 0.5:                
                agents[i]._y  = (agents[i]._y + 1) % 300                
            else:
                agents[i]._y  = (agents[i]._y - 1) % 300

 
    # Show environment    
    plt.imshow(environment)
    # Plot each agent using a blue x
    for i in range(num_of_agents):    
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y, marker='x', color='blue') 

# Create stopping condition
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
carry_on = True

# Create a stopping function for animation 
def gen_function(b = [0]):
    a = 0
    # Not actually needed but clearer
    global carry_on
    while (a < num_of_iterations) & (carry_on):
        # Returns control and waits next call
        yield a
        a = a + 1


# Create function to run the model 
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=gen_function)
    # Use becuase of GUI 
    canvas.draw()
    
    

# SET UP FIGURE 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# Set x and y limits of axes
plt.ylim(0,100)
plt.xlim(0,100)
plt.title("Final Model")
# Set autoscaling on plots
ax.set_autoscale_on(True)



# SET UP GUI
# Build the main window
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


# Build menu bar with option to run model
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)



# WRITE OUT FILES
totalstore = 0 
for agent in agents:
    totalstore = agent.store + totalstore
print("Total consumption:", totalstore)

# Write out environment as file
f2= open('environmentout.csv', 'w', newline='')
writer= csv.writer(f2, delimiter=',')

# Write out total amount stored by each agent
f3= open('agentout.csv', 'w', newline='')
writer= csv.writer(f3, delimiter=',')


for row in environment:
    writer.writerow(row)
f2.close 

tkinter.mainloop()