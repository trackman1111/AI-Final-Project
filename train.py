import gym
import Catan_Env
#import numpy as np
from stable_baselines3 import DQN
from stable_baselines3.common.env_checker import check_env



env = gym.make('Catan-v0')



model = DQN("MlpPolicy",env,verbose=1).learn(10000)

model.save("catanDQN")

env.reset()