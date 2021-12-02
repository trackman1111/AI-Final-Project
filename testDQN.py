from typing import final
import gym
import Catan_Env
from stable_baselines3 import DQN



env = gym.make('Catan-v0')
model = DQN.load("dqn_catan")
obs=env.reset()
gamesRan=0
while gamesRan<20:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    finalIt=env.iteration
    finalCity=env.player.num_cities
    finalSettlements=env.player.num_settlements
    finalRoads= env.player.num_roads
    if done:
        gamesRan+=1
        testString=f"Game number:{gamesRan}. Total number of steps: {finalIt}. Total reward: {reward}.Number of Settlements: {finalSettlements}. Number of Roads:{finalRoads}. Number of Cites:{finalCity} \n"
        resultsFile = open("CatanDQNResults.txt","a")
        resultsFile.write(testString)
        resultsFile.close()
        obs = env.reset() 