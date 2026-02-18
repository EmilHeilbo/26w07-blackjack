"""The current game state, eg. current deck, hands at play, etc."""

import logging
from random import seed, shuffle
from time import sleep
from typing import final
from uuid import UUID

from .card import Card
from .player import Player


@final
class State:
  """Represents the current state of the game, including the deck, players, and dealer."""

  id: UUID
  dealer: Player
  players: list[Player]
  number_of_decks: int
  deck: list[Card] = []

  def get_deck(self, shuffle_deck: bool = True) -> list[Card]:
    """Generates a standard deck of 52 playing cards, with optional shuffling and multiple decks."""
    BASE_DECK = [Card(s, r) for r in Card.Rank for s in Card.Suit]
    DECK = BASE_DECK * max(1, self.number_of_decks)
    if shuffle_deck:
      shuffle(DECK)
    return DECK

  def __init__(self, id: UUID, player_count: int = 1, deck_count: int = 6) -> None:
    self.id = id
    self.number_of_decks = deck_count
    seed(str(id))
    self.deck = self.get_deck()
    self.dealer = Player(0, self.id)
    self.players = [Player(i, self.id) for i in range(1, player_count + 1)]

  def deal_cards(self) -> None:
    """Deals the initial cards to the dealer and players."""
    self.hit(self.dealer)
    for _ in range(2):
      for p in self.players:
        self.hit(p)

  def hit(self, player: Player) -> None:
    """Deals a card to the specified player and updates their score."""
    player.hand.append(self.deck.pop())

  def close(self) -> None:
    """Closes the game by dealing cards to the dealer until they reach a score of 17 or higher."""
    if len(self.top_players) == 1 and self.top_players[0] is not self.dealer:
      while self.dealer.score < 17:
        self.hit(self.dealer)
        logging.info(f"Dealer hits: {self.dealer.hand[-1]}")
        sleep(1)

  @property
  def top_players(self) -> list[Player]:
    """Determines the best hand(s) among the dealer and players, excluding any hands that have busted."""
    ALL_HANDS = [h for h in [self.dealer, *self.players] if h.score <= 21]
    logging.debug(
      f"Hands: {[h.score for h in ALL_HANDS]}, count of hands: {len(ALL_HANDS)}"
    )
    ALL_HANDS.sort(key=lambda x: x.score, reverse=True)
    return [h for h in ALL_HANDS if h.score == ALL_HANDS[0].score]

  def winning_hands_to_string(self) -> str:
    """Converts the winning hand(s) to a string for display."""
    for p in [self.dealer, *self.players]:
      logging.debug(f"Player {str(p.id)} score: {p.score}")
    if len(self.top_players) == 1:
      return "%s wins!" % str(*self.top_players).capitalize()
    WINNERS = (
      self.top_players if len(self.top_players) > 0 else [self.dealer, *self.players]
    )
    return f"Push, {', '.join(str(p) for p in WINNERS)} splits!"
