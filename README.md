# README Agent-Based-Model Practical

## Contents
1. Introduction
3. Sheep in a field
4. Licence

## Introduction
This portfolio has been created for assignment one of the week intensive Leeds University GEOG995 Core programming course. The code was written using Python 3 in the IUD Spyder. 
The [Agent-Based-Model repository](https://github.com/gladyskenyon/Agent-Based-Model) contains the final scripts and outputs. 

There are three key componants to the ABM which all need to be saved in the same directory:
* model.py- contains code to set up and control the model
* agentframework.py- defines the Agent class - object orientated
* in.txt- contains the environment which the agents will interact with    

You will also need to tell the iPython console to produce a popout window by entering 'matplotlib qt' in the console before running the code.

There are three variables which have been set but can be changed:
* number of agents
* number of iterations
* neighbourhood size

## Sheep in a field- what is to be expected
The model represents a field (the environment) which contains a herd of sheep (agents).
The sheep will perform a set of behaviours, as defined in a separate Agent class, which involve interacting with each other and their environment.

There will be 25 sheep which are randomly initialised in the field. The agents move randomly eating the field as they do so. The environment is a torus meaning if the sheep wonder off the field they will return on the other side. The model is animated and is set to iterate 70 times.

The model will  run through a GUI, an external window with a menu from which you can select 'Run Model'. There are 2 other figure pop ups which can be closed.
The rescaling of the colour of the environment represents the sheeps path where they have eaten, it will also show when they have eaten too much and vommited up their store (yellow colour).

Additionally, agents will interact by sharing their store if they come within a certain distance of one another, as defined by the neighbourhood variable.  
The environment values will be written to an excel file. In addition, the total store of all agents will by printed in the console after the model has run.

## Licence 
This project is licenced under the MIT licence.
The website used a theme.
By Gladys Kenyon based on online practicals by Andy Evans.
