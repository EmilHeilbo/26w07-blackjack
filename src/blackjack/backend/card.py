# Here's where all the game logic resides; win-conditions, max dealer score, etc.
from enum import IntEnum
from typing import final, override


@final
class Card:
  """Represents a single card in the deck, with a suit and rank."""

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
  Suit = IntEnum("Suit", SUIT_NAMES)
  Rank = IntEnum("Rank", RANK_NAMES)

  def __init__(self, suit: Suit, rank: Rank) -> None:
    self.suit = suit if type(suit) is self.Suit else self.Suit(suit)
    self.rank = rank if type(rank) is self.Rank else self.Rank(rank)

  @override
  def __repr__(self) -> str:
    return "%s(%s,%s)" % (self.__class__, self.rank.value, self.suit.value)

  @override
  def __str__(self) -> str:
    return "%s of %s" % (self.rank.name, self.suit.name)

  def __int__(self) -> int:
    """Implement int conversion to simplify sorting"""
    return self.suit.value + self.rank.value * 4

  def __lt__(self, other: Card) -> bool:
    return int(self) < int(other)

  @override
  def __eq__(self, other: object) -> bool:
    return int(self) == int(other) if type(other) is self.__class__ else False
