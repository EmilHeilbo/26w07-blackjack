"""The current game state, eg. current deck, hands at play, etc."""

import logging

from .logic import Card, get_deck


class Player:
  """Represents a player in the game, including the dealer."""

  id: int = 0
  hand: list[Card]
  score: int

  def __init__(self, id: int) -> None:
    self.id = id
    self.hand = []
    self.score = 0

  # TODO: Fix edge-case of having three Aces on hand
  # TODO: Implement observer pattern
  def update_score(self) -> None:
    """Updates the player's score based on their current hand."""
    self.score = 0
    for _card in sorted(self.hand, key=lambda card: int(card), reverse=True):
      logging.debug(f"{self.score} before {_card}")
      match _card.rank.value:
        case n if n == 1:
          self.score += 11 if self.score <= 10 else 1
        case n:
          self.score += min(max(n, 1), 10)
      logging.debug(f"{self.score} after {_card}")

  def print_hand(self) -> None:
    name = "Dealer" if self.id == 0 else f"Player {self.id}"
    s = f"{name} hand: {', '.join([str(c) for c in self.hand])}\n{name} score: {self.score}"
    logging.info(s)


class Game_State:
  """Represents the current state of the game, including the deck, players, and dealer."""

  deck: list[Card] = []
  DEALER: Player
  PLAYERS: list[Player]

  def __init__(self, player_count: int = 1) -> None:
    self.deck = get_deck(number_of_decks=6)
    self.DEALER = Player(0)
    self.PLAYERS = [Player(i) for i in range(1, player_count + 1)]

  def deal_cards(self) -> None:
    """Deals the initial cards to the dealer and players."""
    self.DEALER.hand.append(self.deck.pop())
    for _ in range(2):
      for p in self.PLAYERS:
        p.hand.append(self.deck.pop())
    for p in [self.DEALER, *self.PLAYERS]:
      p.update_score()

  def hit(self, player: Player) -> None:
    """Deals a card to the specified player and updates their score."""
    player.hand.append(self.deck.pop())
    player.update_score()

  def close(self) -> None:
    """Closes the game by dealing cards to the dealer until they reach a score of 17 or higher."""
    while self.DEALER.score < 17:
      self.DEALER.hand.append(self.deck.pop())
      self.DEALER.update_score()

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
    WINNERS: list[Player] = [p for p in self.PLAYERS if p in players]
    for p in [self.DEALER, *self.PLAYERS]:
      logging.debug(f"Player {str(p.id)} score: {p.score}")
    if len(WINNERS) == 0 and self.DEALER.score <= 21:
      return "House wins!"
    if (
      (len(WINNERS) == 0 and self.DEALER.score > 21)
      or self.DEALER.score == WINNERS[0].score
      or len(WINNERS) > 1
    ):
      if len(WINNERS) == 0:
        WINNERS = [p for p in self.PLAYERS]
      return f"Push, player {', '.join(str(p.id) for p in WINNERS)} splits!"
    return f"Player {WINNERS[0].id} wins!"
