import matplotlib.pyplot as plt
from networkx.readwrite.graphml import GraphML
import torch
import random
import numpy as np
from collections import deque
from model import QNet, QTrainer
#import helper
#import player
from game_control import GamePlay
#import game

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:

    def __init__(self):
        self.n_games = 0
        self.epsilon = 0 # randomness
        self.gamma = 0.9 # discount rate
        self.memory = deque(maxlen=MAX_MEMORY) # popleft()
        self.model = QNet(9,256, 180)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)

    
    def get_state(self, GamePlay):
        
        player = GamePlay.player
        
        state = [
            
            player.num_settlements,
            player.num_cities,
            player.num_roads,
            GamePlay.score,
            player.num_wood,
            player.num_sheep,
            player.num_brick,
            player.num_wheat,
            player.num_ore
        
            
        ]
            

        return np.array(state, dtype=int)

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done)) # popleft if MAX_MEMORY is reached

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE) # list of tuples
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)
        #for state, action, reward, nexrt_state, done in mini_sample:
        #    self.trainer.train_step(state, action, reward, next_state, done)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state):
        # random moves: tradeoff exploration / exploitation
        self.epsilon = 50 - self.n_games
        final_move = np.full(180,0)
        if random.randint(0, 180) < self.epsilon:
            move = random.randint(0,179 )
            print(state)
            print("Random move is",move)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            print(state)
            move = torch.argmax(prediction).item()
            print("Model move is",move)
            final_move[move] = 1

        return final_move


def train():
    plot_steps = []
    plot_mean_steps = []
    plot_iterations = []
    total_steps = 0
    record = 10000
    agent = Agent()
    game = GamePlay()

    while True:
        # get old state
        state_old = agent.get_state(game)

        # get move
        final_move = agent.get_action(state_old)

        # perform move and get new state
        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)

        # train short memory
        agent.train_short_memory(state_old, final_move, reward, state_new, done)

        # remember
        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            # train long memory, plot result
            
            #reset
            
            agent.n_games += 1
            agent.train_long_memory()

            if game.iteration <  record:
                record = game.iteration
                agent.model.save()

            print('Game', agent.n_games, 'Steps', game.iteration, 'Record:', record)

            plot_steps.append(game.iteration)
            total_steps += game.iteration
            mean_step = total_steps / agent.n_games
            plot_mean_steps.append(mean_step)
            plot_iterations.append(agent.n_games)
            if agent.n_games==50:
                break
            game.reset()
            
    #print(len(plot_iterations))
    #print(len(plot_mean_steps))
    plt.scatter(plot_iterations, plot_steps)
    plt.show()


if __name__ == '__main__':
    train()


def decision():
    return None