import gymnasium as gym
import numpy as np
import time
time.sleep(0.02)

env=gym.make('CartPole',render_mode='human')
#(state,_)=env.reset()
state, info = env.reset(seed=42)

for _ in range(500):
    action = env.action_space.sample()
    state, reward, terminated, truncated, info = env.step(action)
    time.sleep(0.02)
    if terminated or truncated:
        state, info = env.reset()
# env.close()
env.render()
env.step(0)

env.observation_space
env.observation_space.high
env.observation_space.low
env.action_space

env.spec
env.spec.reward_threshold

episodeNumber=100000
timeSteps=100

for episodeIndex in range(episodeNumber):
    initial_state=env.reset()
    print(episodeIndex)
    env.render()
    appendedObservations=[]
    for timeIndex in range (timeSteps):
        print(timeIndex)
        random_action=env.action_space.sample()
        observation,reward,terminated,truncated,info=env.step(random_action)
        appendedObservations.append(observation)
        time.sleep(0.01)
        if(terminated):
            time.sleep(3)
            break
env.close()

