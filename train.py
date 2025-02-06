import rlcard
import time
import torch
import numpy as np
from utils import print_state

env_config = {'seed': 0}
env = rlcard.make('five-hundred', config=env_config)
state, player = env.reset()

for _ in range(13):
  actions = env._get_legal_actions()
  state, player = env.step(actions[0], raw_action=True)

  info = env.game.get_perfect_information()
  print(info, info['tray'].dealer_id)
  print_state(state)