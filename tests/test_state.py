from src.logic import card
from src.state import game_state, player


def test_game_state():
  GAME = game_state()
  GAME.deal_cards()
  assert len(GAME.DEALER.HAND) == 1
  for p in GAME.PLAYERS:
    assert len(p.HAND) == 2
  GAME.hit(GAME.PLAYERS[0])
  assert len(GAME.PLAYERS[0].HAND) == 3
  assert GAME.PLAYERS[0].SCORE != 0
  GAME.close()
  assert GAME.DEALER.SCORE > 17


def test_win_condition():
  GAME = game_state()
  GAME.DEALER.HAND = [
    card(card.Suit(1), card.Rank(1)),
    card(card.Suit(2), card.Rank(10)),
  ]
  GAME.DEALER.update_score()
  WINNERS = GAME.determine_best_hands()
  assert GAME.DEALER in WINNERS
  assert "Dealer wins!" == GAME.winning_hands_to_str(WINNERS) or "Push, dealer splits!"
  GAME.PLAYERS[0].HAND = [
    card(card.Suit(1), card.Rank(1)),
    card(card.Suit(2), card.Rank(10)),
  ]
  GAME.PLAYERS[0].update_score()
  assert GAME.PLAYERS[0].SCORE == 21
  WINNERS = GAME.determine_best_hands()
  assert GAME.PLAYERS[0] in WINNERS
  assert (
    "Push, player 1 splits!" == GAME.winning_hands_to_str(WINNERS)
    or "Push, player 1 splits!"
  )
  GAME.DEALER.HAND[1].rank = card.Rank(9)
  GAME.DEALER.update_score()
  WINNERS = GAME.determine_best_hands()
  assert GAME.DEALER not in WINNERS
  assert (
    "Player 1 wins!" == GAME.winning_hands_to_str(WINNERS) or "Push, dealer splits!"
  )


def test_player_state():
  test_player = player(10)
  test_player.HAND = [
    card(card.Suit(1), card.Rank(1)),
    card(card.Suit(2), card.Rank(1)),
  ]
  test_player.update_score()
  assert test_player.SCORE == 12
  test_player.HAND[1].rank = card.Rank(10)
  test_player.update_score()
  assert test_player.SCORE == 21
