from pettingzoo import ParallelEnv
import gymnasium as gym
import functools
import numpy as np

class rl_env(ParallelEnv):
    metadata = {'render_modes': ['human', 'rgb_array'],
            "render_fps": 30,
            }
    
    def __init__(self, render_mode='rgb_array'):
        self.render_mode = render_mode

        self.agents = ['agent1', 'agent2']
        self.possible_agents = ['agent1', 'agent2']

        # self.actObsType = self.env.getActionObsType() # can be used to change from Box to other types

        # define action and observation spaces
        actionSpace = gym.spaces.Box(low=-1, high=1, shape=(3,), dtype=np.float32)
        self.action_spaces = {agent: actionSpace for agent in self.agents}

        obsSpace = gym.spaces.Box(low=-1, high=1, shape=(3,), dtype=np.float32)
        self.observation_spaces = {agent: obsSpace for agent in self.agents}


    @functools.lru_cache(maxsize=None)
    def action_space(self, agent):
        return self.action_spaces[agent]

    @functools.lru_cache(maxsize=None)
    def observation_space(self, agent):
        return self.observation_spaces[agent]
    
    def close(self):
        pass

    def get_obs(self, agent):
        obs1 = 1.0
        obs2 = 0.5
        obs3 = -1.0

        # TODO: Implement function to get observations for the given agent
        observations = [obs1, obs2, obs3]
        return observations

    def reset(self, seed=None, return_info=False, options=None, **kwargs):
        observations = {}
        infos = {}
        for agent_name in self.agents:
            observations[agent_name] = self.get_obs(agent_name)
            infos[agent_name] = ' '
        return (observations, infos)

    def step(self, actions):
        observations = {}
        rewards = {}
        terminated = {}
        truncated = {}
        info = {}

        # Count to 1000
        for i in range(10000):
            x = 10

        for agent_name in self.agents:
            observations[agent_name] = self.get_obs(agent_name)
            rewards[agent_name] = 0
            terminated[agent_name] = False
            truncated[agent_name] = False
            # info[agent_name] = pybind11.cast("")
        return (observations, rewards, terminated, truncated, info)
