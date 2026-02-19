"""The current game state, eg. current deck, hands at play, etc."""

import logging
from random import seed, shuffle
from sys import modules
from time import sleep
from typing import final
from uuid import UUID

from .card import Card
from .player import Player


@final
class State:
  """Represents the current state of the game, including the deck, players, and dealer."""

  def get_deck(self, shuffle_deck: bool = True) -> list[Card]:
    """Generates a standard deck of 52 playing cards, with optional shuffling and multiple decks."""
    BASE_DECK = [Card(s, r) for r in Card.Rank for s in Card.Suit]
    DECK = BASE_DECK * max(1, self.DECK_COUNT)
    if shuffle_deck:
      shuffle(DECK)
    return DECK

  def __init__(self, id: UUID, player_count: int = 1, deck_count: int = 6) -> None:
    seed(str(id))
    self.ID = id
    self.DECK_COUNT = deck_count
    self.DECK = self.get_deck()
    self.DEALER = Player(0, self.ID)
    self.PLAYERS = [Player(i, self.ID) for i in range(1, player_count + 1)]

  def deal_cards(self) -> None:
    """Deals the initial cards to the dealer and players."""
    self.hit(self.DEALER)
    for _ in range(2):
      for p in self.PLAYERS:
        self.hit(p)

  def hit(self, player: Player) -> None:
    """Deals a card to the specified player and updates their score."""
    player.HAND.append(self.DECK.pop())

  def close(self) -> None:
    """Closes the game by dealing cards to the dealer until they reach a score of 17 or higher."""
    if len(self.top_players) == 1 and self.top_players[0] is not self.DEALER:
      while self.DEALER.score < 17:
        self.hit(self.DEALER)
        logging.info(f"Dealer hits: {self.DEALER.HAND[-1]}")
        if "view.console" in modules:  # pragma: no cover
          sleep(1)

  @property
  def top_players(self) -> list[Player]:
    """Determines the best hand(s) among the dealer and players, excluding any hands that have busted."""
    ALL_HANDS = [h for h in [self.DEALER, *self.PLAYERS] if h.score <= 21]
    logging.debug(
      f"Hands: {[h.score for h in ALL_HANDS]}, count of hands: {len(ALL_HANDS)}"
    )
    ALL_HANDS.sort(key=lambda x: x.score, reverse=True)
    return [h for h in ALL_HANDS if h.score == ALL_HANDS[0].score]

  def winning_hands_to_string(self) -> str:
    """Converts the winning hand(s) to a string for display."""
    for p in [self.DEALER, *self.PLAYERS]:
      logging.debug(f"Player {str(p.ID)} score: {p.score}")
    if len(self.top_players) == 1:
      return "%s wins!" % str(*self.top_players).capitalize()
    WINNERS = (
      self.top_players if len(self.top_players) > 0 else [self.DEALER, *self.PLAYERS]
    )
    return f"Push, {', '.join(str(p) for p in WINNERS)} splits!"
