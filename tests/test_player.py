from backend.card import Card
from backend.player import Player


def test_player_state():
  test_player = Player(10)
  test_player.hand = [
    Card(Card.Suit(1), Card.Rank(1)),
    Card(Card.Suit(2), Card.Rank(1)),
  ]
  assert test_player.score == 12
  test_player.hand[1].rank = Card.Rank(10)
  assert test_player.score == 21
