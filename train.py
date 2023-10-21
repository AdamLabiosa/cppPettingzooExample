from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import VecMonitor, VecNormalize
from stable_baselines3.ppo import MlpPolicy
import envs.rl_env as rl_env
from envs.pytest_env import rl_env as pyrl_env

import supersuit as ss


env = rl_env.rl_env('test_env')
# env = pyrl_env()

env = ss.pettingzoo_env_to_vec_env_v1(env)
env = ss.concat_vec_envs_v1(env, num_vec_envs=2, num_cpus=1, base_class='stable_baselines3')
env = VecMonitor(env) 
env = VecNormalize(env, norm_obs=False, norm_reward=True, clip_obs=10)

model = PPO(MlpPolicy, env, verbose=1, batch_size=10000)

model.learn(total_timesteps=100000)
