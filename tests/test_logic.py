from src.logic import Card, get_deck


def test_correct_deck_size():
  for n in range(6):
    # Correct for not including end of range, starting at 0
    COUNT = n + 1
    EXPECTED_DECK_SIZE = 52
    assert len(get_deck(COUNT)) == EXPECTED_DECK_SIZE * COUNT


def test_ensure_shuffle_works():
  DECK = get_deck()
  UNSHUFFLED_DECK = get_deck(shuffle_deck=False)
  print("The top card is the ", DECK[-1])
  assert DECK != UNSHUFFLED_DECK
  assert sorted(DECK) == UNSHUFFLED_DECK


def test_card_functions():
  ACE_OF_SPADES = Card(Card.Suit(1), Card.Rank(1))
  assert str(ACE_OF_SPADES) == "Ace of Spades"
  assert repr(ACE_OF_SPADES) == "<class 'src.logic.Card'>(1,1)"
