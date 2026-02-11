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
  GAME.DEALER.update_score()
  WINNERS = GAME.determine_best_hands()
  assert GAME.DEALER in WINNERS
  assert (
    "Dealer wins!" == GAME.winning_hands_to_string(WINNERS) or "Push, dealer splits!"
  )
  GAME.PLAYERS[0].hand = [
    Card(Card.Suit(1), Card.Rank(1)),
    Card(Card.Suit(2), Card.Rank(10)),
  ]
  GAME.PLAYERS[0].update_score()
  assert GAME.PLAYERS[0].score == 21
  assert (
    GAME.PLAYERS[0].print_hand()
    == "Player 1 hand: Ace of Spades, Ten of Hearts\nPlayer 1 score: 21"
  )
  WINNERS = GAME.determine_best_hands()
  assert GAME.PLAYERS[0] in WINNERS
  assert (
    "Push, player 1 splits!" == GAME.winning_hands_to_string(WINNERS)
    or "Push, player 1 splits!"
  )
  GAME.DEALER.hand[1].rank = Card.Rank(9)
  GAME.DEALER.update_score()
  WINNERS = GAME.determine_best_hands()
  assert GAME.DEALER not in WINNERS
  assert (
    "Player 1 wins!" == GAME.winning_hands_to_string(WINNERS)
    or "Push, Player 1 splits!"
  )


def test_player_state():
  test_player = Player(10)
  test_player.hand = [
    Card(Card.Suit(1), Card.Rank(1)),
    Card(Card.Suit(2), Card.Rank(1)),
  ]
  test_player.update_score()
  assert test_player.score == 12
  test_player.hand[1].rank = Card.Rank(10)
  test_player.update_score()
  assert test_player.score == 21
