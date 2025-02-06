import rlcard

from rlcard.games.five_hundred.utils.five_hundred_card import FiveHundredCard
from rlcard.games.five_hundred.utils.action_event import ActionEvent

# Score:            2 [our_score, their_score]
# Game phase:       3 [bidding, discarding, playing]
# Hand:             43 [4S, 4C, 5S, ..., AD, AH, JK] (one hot)
# Bid(s):           27 [6S, 6C, ..., 8S, M, 8C, ... 10H, 10NT, OM] (one hot)
# Player position:  4 [0, 1, 2, 3] (one hot)
# Passed players:   4 [0, 1, 2, 3] (one hot)
# Tricks won:       10 [1, 2, ..., 10] (one hot)
# Trick cards:      43 [4S, 4C, 5S, ..., AD, AH, JK] (1, 2, 3 in order)
# Opponent's hand   43              '                (if open misere)
# TOTAL:            136

def print_state(state):

  # Score and phase
  print("********* PRINTING STATE *********\n")
  print(f"Score: {state[0]} : {state[1]}")
  print("Phase: ", end='')
  if state[2]: print("BID")
  elif state[3]: print("DISCARD")
  elif state[4]: print("PLAY")
  else: print("OVER")

  # Hand
  print("Hand: ", end='')
  print([FiveHundredCard.card(i-5) for i in range(5, 48) if state[i]])

  # Bids
  print("Bids: ", end='')
  print([ActionEvent.from_action_id(i - 48 + 2) for i in range(48, 75) if state[i]])

  # Player position
  print(f"Player position: ", end = '')
  print(next(i - 75 for i in range(75, 79) if state[i]))

  # Passed players
  print(f"Passed players: ", end = '')
  print([i - 79 for i in range(79, 83) if state[i]])

  # Tricks won
  print(f"Tricks won: ", end = '')
  print(state[83:93])

  # Trick cards
  trick_card_ids = [None] * 3
  print(f"Trick cards: ", end = '')
  print()
  for i, pos in enumerate(state[93:136]):
    if pos:
      print("i = ", i)
      print("pos = ", pos)
      if pos < 4:
        trick_card_ids[int(pos)-1] = i
  print(trick_card_ids)


  # Opponents hand
  print("Opponents hand: ", end='')
  print([FiveHundredCard.card(i-5) for i in range(136, 179) if state[i]])
  print()
  print("*********   END STATE    *********")