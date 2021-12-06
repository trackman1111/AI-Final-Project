# AI-Final-Project

The network has an input layer of 9, a hidden layer of 256, and an output layer of 180 with its activation being ReLU. A class within py.model is used to take the model and optimize it using the Adam optimization. We also train the next step using the Bellman equation to pick the action with the highest reward value. We later incorporated the Epsilon-Greedy Policy in the agent which allowed the agent to balance exploration and exploitation by choosing between exploration and exploitation randomly. The agent.py holds the long term and short term memory. The agent then runs the game for the given amount of time. For every turn it adds to the short term memory and for every game finished it adds to the long term memory. The agent also keeps up with the amount of steps taken in a game, so if a game’s steps are lower than the record the model is updated to the one from the current game.


# Files

edges.txt, nodes.txt, hex.py

Edges.txt and nodes.txt are configuration files used to enumerate the hex linkages seen in the game board. They include the information necessary for making the connections within the data structure displayed in hex.py that match a specific game board set beforehand.

game board.py

Game_board.py contains all the necessary algorithms for facilitating game board state changes. Implementing a game board that relies on foundational AI algorithms ensures that efficient building and traversal of the hexagonal game board takes place. Breadth first search algorithms proved especially important as it is used to send optimal path data for prospective settlement locations. The AI uses this data to compare the different build path values and weights when deciding which node or edge to build on next.

player.py
    
This file facilitates player actions within the game while keeping track of player information. Each player's actions has the possibility of altering the amount of resources, settlements, roads, and cities within a player's ownership. A player is initialized with starting resources, roads, and settlements.

game_control.py

The game_control.py connects the player and game board so that any game state changes during game progression reconstruct player and game boards to match. This file is Agent’s way of interacting with the game. As the name implies this is the center point for the entire system. 

agent.py

The agent.py holds the long term and short term memory. The agent then runs the game for the given amount of time. For every turn it adds to the short term memory and for every game finished it adds to the long term memory. The agent also keeps up with the amount of steps taken in a game, so if a game’s steps are lower than the record the model is updated to the one from the current game.

model.py

The model.py creates the Neural Network for using Pytorch. The Neural Network has 9 input neurons, 256 neurons in the hidden layer, and 180 neurons in the output layer. The QTrainer function optimizes the model and takes inputs from the agent to find the best step using the Bellman equations.
