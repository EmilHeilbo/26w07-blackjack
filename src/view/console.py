import logging
from time import sleep
from typing import final
from uuid import uuid4

from backend.state import State


@final
class ConsoleView:
  """Implements the console interface for the Blackjack game."""

  state = State(uuid4())

  def run(self):
    """Runs the console interface for the Blackjack game."""
    _intro_text = """
    Welcome to Blackjack!
    Rules:
      - The goal is to get as close to 21 as possible without going over.
      - You can hit (take another card) or stand (keep your current hand).
      - The dealer hits until they reach 17 or higher.
      - The game stands automatically when the player's score is 21 or higher.

      ------------------
    """.strip()
    logging.info(_intro_text)
    self.state.deal_cards()
    for p in [self.state.dealer, *self.state.players]:
      p.print_hand()
      logging.info("------------------")
    self.state.hit(self.state.dealer)

    _input = None
    while _input != "s" and self.state.players[0].score < 21:
      _input = input("Enter 'h' to hit or 's' to stand: ")
      match _input:
        case "h":
          logging.debug("Player hits.")
          self.state.hit(self.state.players[0])
          if self.state.players[0].score == 21:
            logging.info(f"{str(self.state.players[0]).capitalize()} has blackjack!")
          else:
            self.state.players[0].print_hand()
        case "s":
          logging.debug("Player stands.")
        case _:
          logging.info("Invalid input. Please enter 'h' or 's'.")
      logging.info("------------------")
      sleep(1)

    self.state.close()
    self.state.dealer.print_hand()
    logging.info("------------------")
    logging.info(self.state.winning_hands_to_string())
