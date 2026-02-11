# Here's where all the game logic resides; win-conditions, max dealer score, etc.
from enum import Enum
from random import shuffle


class card:
  # Separate value names from logic, to make future localization easier
  SUIT_NAMES = ["Spades", "Hearts", "Clubs", "Diamonds"]
  RANK_NAMES = [
    "Ace",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
  ]
  Suit = Enum("Suit", SUIT_NAMES)
  Rank = Enum("Rank", RANK_NAMES)

  def __init__(self, suit: Suit = Suit(1), rank: Rank = Rank(1)) -> None:
    self.suit = suit if type(suit) is self.Suit else self.Suit(suit)
    self.rank = rank if type(rank) is self.Rank else self.Rank(rank)

  def __repr__(self) -> str:
    return "%s(%s,%s)" % (self.__class__, self.rank.value, self.suit.value)

  def __str__(self) -> str:
    return "%s of %s" % (self.rank.name, self.suit.name)

  # Implement int conversion to simplify sorting
  def __int__(self) -> int:
    return self.suit.value + self.rank.value * 4

  def __lt__(self, other) -> bool:
    return int(self) < int(other)

  def __eq__(self, other) -> bool:
    return int(self) == int(other)


def get_deck(number_of_decks: int = 1, shuffle_deck: bool = True) -> list[card]:
  BASE_DECK = [card(s, r) for r in card.Rank for s in card.Suit]
  DECK = BASE_DECK * max(1, number_of_decks)
  if shuffle_deck:
    shuffle(DECK)
  return DECK
