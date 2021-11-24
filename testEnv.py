import gym
import Catan_Env

env = gym.make('Catan-v0')

# Box(4,) means that it is a Vector with 4 components
print("Observation space:", env.observation_space)
#print("Shape:", env.observation_space.shape)
# Discrete(2) means that there is two discrete actions
print("Action space:", env.action_space)