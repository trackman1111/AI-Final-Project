from gym import Env
from gym import spaces
from gym.spaces import Discrete,Box
import numpy as np
import random
from game_control import GamePlay
import tensorflow
from stable_baselines.common.env_checker import check_env
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam
import rl
from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory


class CatanGame(Env):
    def _init_(self):
        #31+40+roll+updgradeCity+endturn
        self.catanGame= GamePlay()
        
        self.action_space = spaces.Discrete(180)
        #settlments cities roads points resources
        self.observation_space = spaces.Box(low=np.array([0,0,0,0,0,0,0,0,0]),high=np.array([5,4,15,10,5,5,5,5,5]),dytpe=np.float32)
    
    def step(self,action):
        reward=self.catanGame.step(action)
        score = self.catanGame.player.score
        obs=[self.catanGame.player.num_settlement,self.catanGame.player.num_cities,
             self.catanGame.player.num_road,score,self.catanGame.player.num_sheep,
            self.catanGame.player.num_wheat,self.catanGame.player.num_wood,
            self.catanGame.player.num_brick,self.catanGame.player.num_ore ]
        done = bool(self.score==10)
        return obs,reward,done,{}

    def render(self):
        pass
    
    def reset(self):
        del self.catanGame
        self.catanGame = GamePlay()
        obs = [0,0,0,0,0,0,0,0,0]
        return obs
    
env = CatanGame()
# If the environment don't follow the interface, an error will be thrown
check_env(env, warn=True)

obs = env.reset()


print(env.observation_space)
print(env.action_space)
print(env.action_space.sample())


num_actions = env.action_space.n
for t in range(500):
    act= env.action_space.sample()
    obs,reward,done,info=env.setp(act)
    if done:
        print("Game over you got 10 points")
        
#Agent

agent = Sequential()
agent.add(Flatten(input_shape =(1, ) + env.observation_space.shape))
agent.add(Dense(16))
agent.add(Activation('relu'))
agent.add(Dense(num_actions))
agent.add(Activation('linear'))


#Model
policy= EpsGreedyQPolicy(eps=0.3)
memory = SequentialMemory(limit = 10000, window_length = 1)

dqn = DQNAgent(model = agent,
               nb_actions = num_actions,
               memory = memory, 
               nb_steps_warmup = 10,
               target_model_update = 1e-2,
               policy = policy)
dqn.compile(Adam(lr = 1e-3), metrics =['mae'])


#traning
dqn.fit(env, nb_steps = 5000, visualize = False, verbose = 2)

#testing
dqn.test(env, nb_episodes = 5, visualize = True)