import logging

from src.card import Card
from src.state import State


def test_correct_deck_size():
  for n in range(6):
    # Correct for not including end of range, starting at 0
    COUNT = n + 1
    EXPECTED_DECK_SIZE = 52
    assert len(State(deck_count=COUNT).get_deck()) == EXPECTED_DECK_SIZE * COUNT


def test_ensure_shuffle_works():
  DECK = State(deck_count=1).get_deck()
  UNSHUFFLED_DECK = State(deck_count=1).get_deck(shuffle_deck=False)
  logging.info("The top card is the ", DECK[-1])
  assert DECK != UNSHUFFLED_DECK
  assert sorted(DECK) == UNSHUFFLED_DECK


def test_card_functions():
  ACE_OF_SPADES = Card(Card.Suit(1), Card.Rank(1))
  assert str(ACE_OF_SPADES) == "Ace of Spades"
  assert repr(ACE_OF_SPADES) == "<class 'src.card.Card'>(1,1)"
