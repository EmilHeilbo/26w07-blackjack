"""The current game state, eg. current deck, hands at play, etc."""

import logging
from random import shuffle
from time import sleep
from uuid import UUID, uuid4

from .card import Card
from .player import Player


class State:
  """Represents the current state of the game, including the deck, players, and dealer."""

  ID: UUID
  DEALER: Player
  PLAYERS: list[Player]
  NUMBER_OF_DECKS: int
  deck: list[Card] = []

  def get_deck(self, shuffle_deck: bool = True) -> list[Card]:
    """Generates a standard deck of 52 playing cards, with optional shuffling and multiple decks."""
    BASE_DECK = [Card(s, r) for r in Card.Rank for s in Card.Suit]
    DECK = BASE_DECK * max(1, self.NUMBER_OF_DECKS)
    if shuffle_deck:
      shuffle(DECK)
    return DECK

  def __init__(self, player_count: int = 1, deck_count: int = 6) -> None:
    self.ID = uuid4()
    self.NUMBER_OF_DECKS = deck_count
    self.deck = self.get_deck()
    self.DEALER = Player(0)
    self.PLAYERS = [Player(i) for i in range(1, player_count + 1)]

  def deal_cards(self) -> None:
    """Deals the initial cards to the dealer and players."""
    self.DEALER.hand.append(self.deck.pop())
    for _ in range(2):
      for p in self.PLAYERS:
        p.hand.append(self.deck.pop())

  def hit(self, player: Player) -> None:
    """Deals a card to the specified player and updates their score."""
    player.hand.append(self.deck.pop())

  def close(self) -> None:
    """Closes the game by dealing cards to the dealer until they reach a score of 17 or higher."""
    while self.DEALER.score < 17:
      self.DEALER.hand.append(self.deck.pop())
      logging.info(f"Dealer hits: {self.DEALER.hand[-1]}")
      sleep(1)

  def determine_best_hands(self) -> list[Player]:
    """Determines the best hand(s) among the dealer and players, excluding any hands that have busted."""
    ALL_HANDS = [h for h in [self.DEALER, *self.PLAYERS] if h.score <= 21]
    logging.debug(
      f"Hands: {[h.score for h in ALL_HANDS]}, count of hands: {len(ALL_HANDS)}"
    )
    ALL_HANDS.sort(key=lambda x: x.score, reverse=True)
    return [h for h in ALL_HANDS if h.score == ALL_HANDS[0].score]

  def winning_hands_to_string(self, players: list[Player]) -> str:
    """Converts the winning hand(s) to a string for display."""
    for p in [self.DEALER, *self.PLAYERS]:
      logging.debug(f"Player {str(p.id)} score: {p.score}")
    if len(players) == 1:
      return "%s wins!" % str(players[0]).capitalize()
    WINNERS = players if len(players) > 0 else [self.DEALER, *self.PLAYERS]
    return f"Push, player {', '.join(str(p.id) for p in WINNERS)} splits!"
