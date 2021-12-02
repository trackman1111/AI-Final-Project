import gym
import Catan_Env
#import tensorflow
from stable_baselines3 import DQN


env = gym.make('Catan-v0')

# Box(4,) means that it is a Vector with 4 components
#print("Observation space:", env.observation_space)
#print("Shape:", env.observation_space.shape)
# Discrete(2) means that there is two discrete actions
#print("Action space:", env.action_space)

obs = env.reset()
# Sample a random action
#action = env.action_space.sample()
#print("Sampled action:", action)
#obs, reward, done, info = env.step(action)
# Note the obs is a numpy array
# info is an empty dict for now but can contain any debugging info
# reward is a scalar
#print(obs, reward, done, info)


#print(env.observation_space)
#print(env.action_space)
#print(env.action_space.sample())

# Hardcoded best agent: always go left!
""" n_steps = 100
for step in range(n_steps):
    action=env.action_space.sample()
    print("Step {}".format(step + 1))
    obs, reward, done, info = env.step(action)
    print('obs=', obs, 'reward=', reward, 'done=', done)
    if done:
        print("Goal reached!", "reward=", reward)
        break """
     

model = DQN("CnnPolicy", env, verbose=1)
model.learn(total_timesteps=10000, log_interval=4)
model.save("dqn_catanCNN")

#del model # remove to demonstrate saving and loading
del model

""" model = DQN.load("dqn_catan")

gamesRan=0
while gamesRan<10:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    finalIt=env.iteration
    if done:
        gamesRan+=1
        testString=f"Game number:{gamesRan}. Total number of steps: {finalIt}. Total reward: {reward}. \n"
        resultsFile = open("CatanResults.txt","a")
        resultsFile.write(testString)
        resultsFile.close()
        obs = env.reset()  """