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
    self.set = set
    self.number = number

  def __repr__(self):
    return "(%s,%s)" % (self.set, self.number)

  def __str__(self) -> str:
    return "%s of %s" % (self.number.name, self.set.name)


def get_deck(number_of_decks: int = 1, shuffle_deck: bool = True):
  deck = []
  for s in card.Set:
    for n in card.Number:
      print(f"Adding {card(s, n)}")
      deck.append(card(s, n))
  for _ in range(1, number_of_decks):
    deck += deck[:52]
  if shuffle_deck:
    shuffle(deck)
  return deck
