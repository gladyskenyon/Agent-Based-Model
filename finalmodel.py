# IMPORT LIBRARIES
import random # For random number generation
import matplotlib.pyplot as plt # For plotting, use shorthand 
from matplotlib.animation import FuncAnimation # For animation
import tkinter # For GUI programming
import csv # For reading in csv files
import agentframework1 # Contains the Agent class
import matplotlib # For mapping 
matplotlib.use('TkAgg') # For creating GUI


# SET VARIABLES   
# For the number of sheep (agents)
num_of_agents = 25
# For the number of times the model iterates
num_of_iterations = 70
# For the proximity of sheep to share resources with others
neighbourhood = 20                                                                                                                 

# Create empty environment list                                
environment = []
# Create empty list for agents                                                 
agents = []


# CREATE THE ENVIRONMENT - FIELD FOR SHEEP 
# Use CSV reader code to open and read in text file
f = open('in.txt', newline = '')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)

# Shift environment into a 2.D. list
for row in reader:	# For every row
    rowlist = [] # Create an empty rowlist
    for value in row:  
        rowlist.append(value) # Attach all values to rowlist
    environment.append(rowlist) # Attach rowlist to environment
    plt.savefig('Field') # Save the figure
f.close() # Good practice to close file    


# CREATE THE AGENTS - SHEEP TO GRAZE FIELD
# Give each agent access to info on others
for i in range(num_of_agents):
    agents.append(agentframework1.Agent(environment, agents, neighbourhood))

# Check the agentframework file is connected using print function
a = agentframework1.Agent(environment, agents, neighbourhood)
# print(a._y, a._x)
a.move() # Check the co-ordinates move
# print(a._y, a._x)


# SET UP THE MODEL
fig = plt.figure(figsize=(14, 14)) # Set figure size using matplotlib

def update(frame_number):  # Define update function by frame_number
    global carry_on      
    fig.clear() # Clear figure     
    plt.imshow(environment) # Show field       
    random.shuffle(agents) # Randomise order of actions
    
    # For each agent initialize behaviour from agentframework1       
    for i in range(num_of_agents):  
                       
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        agents[i].sick()
    
    # Plot the sheep 
    for i in range(num_of_agents):  # For every agent  
            plt.scatter(agents[i]._x,agents[i]._y, marker='*', color="white", 
                        s=100) # Plot using a white star  
            
    # Edit how the figure looks  
    plt.ylim(0,100) # Y axis length
    plt.xlim(0,100) # X axis length
    plt.ylabel("Grass field") # Set y axis label
    plt.xlabel("Grass field") # Set x axis label
    plt.title("An Agent Based Model depicting sheep grazing a field", fontsize='xx-large') # Choose title
    plt.legend(["Sheep"], loc = "upper center") # Choose legend and location
    

# ANIMATE THE MODEL
def run(): # Define run function
    # Use FuncAnimation to set the frames to number of iterations
    animation = matplotlib.animation.FuncAnimation(fig, update,
                                                   frames= num_of_iterations, repeat = False)        
    canvas.draw() # Draw the figure
 
    
# SET UP GUI
# Build the main window
root = tkinter.Tk()
root.wm_title("ABM") # Set window title to ABM
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root) #
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Build menu bar with option to run model
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop() # Sets the GUI waiting for events



# Write out environment as file
f2= open('environmentout.csv', 'a', newline='') # Open csv file
writer= csv.writer(f2, delimiter=',') # Use csv writer
for row in environment: 
    writer.writerow(row) 
f2.close() # Close file 

# Work out total stored by all agents
totalstore = 0 
for agent in agents:
    totalstore = agent.store + totalstore
print("Total consumption:", totalstore) # Print total store
