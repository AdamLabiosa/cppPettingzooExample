from pettingzoo import ParallelEnv
import gymnasium as gym
import functools
import numpy as np
import test_env



class rl_env(ParallelEnv):
    metadata = {'render_modes': ['human', 'rgb_array'],
            "render_fps": 30,
            }
    
    def __init__(self, env, render_mode='rgb_array'):
        if env == 'test_env':
            self.env = test_env
        else:
            raise NotImplementedError

        self.render_mode = render_mode

        self.agents = self.env.get_agents()
        self.possible_agents = self.env.get_agents()

        self.actObsType = self.env.getActionObsType() # can be used to change from Box to other types

        # define action and observation spaces
        actionSpace = self.env.getActionSpace()
        actionSpace = gym.spaces.Box(low=np.array(actionSpace[0]), high=np.array(actionSpace[1]), dtype=np.float32)
        self.action_spaces = {agent: actionSpace for agent in self.agents}

        obsSpace = self.env.getObservationSpace()
        obsSpace = gym.spaces.Box(low=np.array(obsSpace[0]), high=np.array(obsSpace[1]), dtype=np.float32)
        self.observation_spaces = {agent: obsSpace for agent in self.agents}


    @functools.lru_cache(maxsize=None)
    def action_space(self, agent):
        return self.action_spaces[agent]

    @functools.lru_cache(maxsize=None)
    def observation_space(self, agent):
        return self.observation_spaces[agent]
    
    def close(self):
        pass

    def reset(self, seed=None, return_info=False, options=None, **kwargs):
        observations, infos = self.env.reset()
        infos = {agent: ' ' for agent in self.agents}
        return observations, infos

    def step(self, actions):
        obs, rew, terminated, truncated, info = self.env.step(actions)
        return obs, rew, terminated, truncated, info
