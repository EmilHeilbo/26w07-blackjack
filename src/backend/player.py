import logging
from typing import final, override
from uuid import UUID

from .card import Card


@final
class Player:
  """Represents a player in the game, including the dealer."""

  def __init__(self, id: int, game_id: UUID) -> None:
    self.GAME_ID = game_id
    self.ID = id
    self.HAND: list[Card] = []

  @override
  def __str__(self) -> str:
    return f"player {self.ID}" if self.ID else "house"

  @property
  def score(self) -> int:
    """Updates the player's score based on their current hand."""
    score = 0
    for i, _card in enumerate(
      sorted(self.HAND, key=lambda card: int(card), reverse=True)
    ):
      match _card.rank.value:
        case n if n == 1:
          score += 11 if score + len(self.HAND[i + 1 :]) <= 10 else 1
        case n:
          score += min(max(n, 1), 10)
      logging.debug(f"{score} after {_card}")
    return score

  def print_hand(self) -> None:
    logging.info(
      f"{str(self).capitalize()} hand: {', '.join([str(c) for c in self.HAND])}"
    )
    logging.info(f"  Score: {self.score}")
