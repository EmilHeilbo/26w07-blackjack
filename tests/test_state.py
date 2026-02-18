from uuid import UUID

from backend.state import State

# Assign UUID to ensure dealer plays
PLAYER_WIN_ID = UUID("cb548291-a4c2-4786-ac1a-33e293ddcd0e")
HOUSE_WIN_ID = UUID("6a5e0e4e-2285-4ce2-bdab-26298c14498c")
PUSH_ID = UUID("2dde7f9a-c0eb-4521-9b37-249f9ffef326")


def test_game_state():
  GAME = State(PLAYER_WIN_ID)
  GAME.deal_cards()
  assert len(GAME.DEALER.HAND) == 1
  for p in GAME.PLAYERS:
    assert len(p.HAND) == 2
  GAME.hit(GAME.PLAYERS[0])
  assert len(GAME.PLAYERS[0].HAND) == 3
  assert GAME.PLAYERS[0].score != 0
  GAME.close()
  assert GAME.DEALER.score >= 17
  assert GAME.DEALER not in GAME.top_players
  assert GAME.winning_hands_to_string() == "Player 1 wins!"


def test_house_win():
  GAME = State(HOUSE_WIN_ID)
  GAME.deal_cards()
  while GAME.PLAYERS[0].score < 17:
    GAME.hit(GAME.PLAYERS[0])
  GAME.close()
  assert GAME.DEALER in GAME.top_players
  assert GAME.winning_hands_to_string() == "House wins!"


def test_push():
  GAME = State(PUSH_ID)
  GAME.deal_cards()
  while GAME.PLAYERS[0].score < 17:
    GAME.hit(GAME.PLAYERS[0])
  GAME.close()
  GAME.PLAYERS[0].print_hand()
  assert [GAME.DEALER, *GAME.PLAYERS] == GAME.top_players
  assert GAME.winning_hands_to_string() == "Push, house, player 1 splits!"
