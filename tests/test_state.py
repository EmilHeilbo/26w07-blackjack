from src.logic import Card
from src.state import Game_State, Player


def test_game_state():
  GAME = Game_State()
  GAME.deal_cards()
  assert len(GAME.DEALER.hand) == 1
  for p in GAME.PLAYERS:
    assert len(p.hand) == 2
  GAME.hit(GAME.PLAYERS[0])
  assert len(GAME.PLAYERS[0].hand) == 3
  assert GAME.PLAYERS[0].score != 0
  GAME.close()
  assert GAME.DEALER.score >= 17


def test_win_condition():
  GAME = Game_State()
  GAME.DEALER.hand = [
    Card(Card.Suit(1), Card.Rank(1)),
    Card(Card.Suit(2), Card.Rank(10)),
  ]
  WINNERS = GAME.determine_best_hands()
  assert GAME.DEALER in WINNERS
  assert (
    "Dealer wins!" == GAME.winning_hands_to_string(WINNERS) or "Push, dealer splits!"
  )
  GAME.PLAYERS[0].hand = [
    Card(Card.Suit(1), Card.Rank(1)),
    Card(Card.Suit(2), Card.Rank(10)),
  ]
  assert GAME.PLAYERS[0].score == 21
  GAME.PLAYERS[0].print_hand()
  WINNERS = GAME.determine_best_hands()
  assert GAME.PLAYERS[0] in WINNERS
  assert (
    "Push, player 1 splits!" == GAME.winning_hands_to_string(WINNERS)
    or "Push, player 1 splits!"
  )
  GAME.DEALER.hand[1].rank = Card.Rank(9)
  WINNERS = GAME.determine_best_hands()
  assert GAME.DEALER not in WINNERS
  WIN_STRING = GAME.winning_hands_to_string(WINNERS)
  assert WIN_STRING in ["Push, Player 1 splits!", "Player 1 wins!"]


def test_player_state():
  test_player = Player(10)
  test_player.hand = [
    Card(Card.Suit(1), Card.Rank(1)),
    Card(Card.Suit(2), Card.Rank(1)),
  ]
  assert test_player.score == 12
  test_player.hand[1].rank = Card.Rank(10)
  assert test_player.score == 21
