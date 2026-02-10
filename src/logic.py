# Here's where all the game logic resides; win-conditions, max dealer score, etc.
from enum import Enum
from random import shuffle


class card:
  # Separate value names from logic, to make future localization easier
  SET_NAMES = ["Spades", "Hearts", "Clubs", "Diamonds"]
  CARD_NAMES = [
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
  Set = Enum("Set", SET_NAMES)
  Number = Enum("Number", CARD_NAMES)

  def __init__(self, set: Set = Set(1), number: Number = Number(1)) -> None:
    self.set = set if type(set) is self.Set else self.Set(set)
    self.number = number if type(number) is self.Number else self.Number(number)

  def __repr__(self) -> str:
    return "%s(%s,%s)" % (self.__class__, self.number.value, self.set.value)

  def __str__(self) -> str:
    return "%s of %s" % (self.number.name, self.set.name)

  # Implement int conversion to simplify sorting
  def __int__(self) -> int:
    return self.set.value * 13 + self.number.value

  def __lt__(self, other) -> bool:
    return int(self) < int(other)

  def __eq__(self, other) -> bool:
    return int(self) == int(other)


def get_deck(number_of_decks: int = 1, shuffle_deck: bool = True) -> list[card]:
  deck: list[card] = []
  for s in card.Set:
    for n in card.Number:
      deck.append(card(s, n))
  for _ in range(1, number_of_decks):
    deck += deck[:52]
  if shuffle_deck:
    shuffle(deck)
  return deck
