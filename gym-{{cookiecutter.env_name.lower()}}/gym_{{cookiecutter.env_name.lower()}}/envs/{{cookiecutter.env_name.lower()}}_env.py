import gym
from gym import error, spaces, utils
from gym.utils import seeding

class {{cookiecutter.env_name}}Env(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
      raise NotImplementedError
  def step(self, action):
      raise NotImplementedError
  def reset(self):
      raise NotImplementedError
  def render(self, mode='human', close=False):
      raise NotImplementedError
