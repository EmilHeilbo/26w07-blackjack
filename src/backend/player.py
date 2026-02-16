import logging

from .state import Card


class Player:
  """Represents a player in the game, including the dealer."""

  id: int = 0
  hand: list[Card]

  def __init__(self, id: int) -> None:
    self.id = id
    self.hand = []

  def __str__(self) -> str:
    return f"player {self.id}" if self.id else "house"

  @property
  def score(self) -> int:
    """Updates the player's score based on their current hand."""
    score = 0
    for i, _card in enumerate(
      sorted(self.hand, key=lambda card: int(card), reverse=True)
    ):
      logging.debug(f"{score} before {_card}")
      match _card.rank.value:
        case n if n == 1:
          score += 11 if score + len(self.hand[i + 1 :]) <= 10 else 1
        case n:
          score += min(max(n, 1), 10)
      logging.debug(f"{score} after {_card}")
    return score

  def print_hand(self) -> None:
    logging.info(
      f"{str(self).capitalize()} hand: {', '.join([str(c) for c in self.hand])}"
    )
    logging.info(f"  Score: {self.score}")
