from uuid import uuid4

from backend.card import Card
from backend.state import State


def test_game_state():
  GAME = State(uuid4())
  GAME.deal_cards()
  assert len(GAME.dealer.hand) == 1
  for p in GAME.players:
    assert len(p.hand) == 2
  GAME.hit(GAME.players[0])
  assert len(GAME.players[0].hand) == 3
  assert GAME.players[0].score != 0
  GAME.close()
  assert GAME.dealer.score >= 17


def test_win_condition():
  GAME = State(uuid4())
  GAME.dealer.hand = [
    Card(Card.Suit(1), Card.Rank(1)),
    Card(Card.Suit(2), Card.Rank(10)),
  ]
  assert GAME.dealer in GAME.top_players
  assert "Dealer wins!" == GAME.winning_hands_to_string() or "Push, dealer splits!"
  GAME.players[0].hand = [
    Card(Card.Suit(1), Card.Rank(1)),
    Card(Card.Suit(2), Card.Rank(10)),
  ]
  assert GAME.players[0].score == 21
  GAME.players[0].print_hand()
  assert GAME.players[0] in GAME.top_players
  assert (
    "Push, player 1 splits!" == GAME.winning_hands_to_string()
    or "Push, player 1 splits!"
  )
  GAME.dealer.hand[1].rank = Card.Rank(9)
  assert GAME.dealer not in GAME.top_players
  WIN_STRING = GAME.winning_hands_to_string()
  assert WIN_STRING in ["Push, Player 1 splits!", "Player 1 wins!"]
