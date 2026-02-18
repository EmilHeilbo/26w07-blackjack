import logging
from uuid import uuid4

from backend.card import Card
from backend.state import State


def test_correct_deck_size():
  for n in range(6):
    # Correct for not including end of range, starting at 0
    COUNT = n + 1
    EXPECTED_DECK_SIZE = 52
    assert (
      len(State(uuid4(), deck_count=COUNT).get_deck()) == EXPECTED_DECK_SIZE * COUNT
    )


def test_ensure_shuffle_works():
  STATE = State(uuid4(), deck_count=1)
  logging.info("The top card is the %s", STATE.DECK[-1])
  assert STATE.DECK != sorted(STATE.DECK)
  assert sorted(STATE.DECK) == STATE.get_deck(shuffle_deck=False)


def test_card_functions():
  ACE_OF_SPADES = Card(Card.Suit(1), Card.Rank(1))
  assert str(ACE_OF_SPADES) == "Ace of Spades"
  assert repr(ACE_OF_SPADES) == "<class 'backend.card.Card'>(1,1)"
