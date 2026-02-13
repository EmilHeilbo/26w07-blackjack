import logging
from time import sleep

from ..state import Game_State


class ConsoleView(Game_State):
  """Implements the console interface for the Blackjack game."""

  STATE: Game_State

  def __init__(self, state):
    self.state = state

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
    """
    logging.info(_intro_text)
    self.state.deal_cards()
    for p in [self.state.DEALER, *self.state.PLAYERS]:
      p.print_hand()
      logging.info("------------------")

    _input = None
    while _input != "s" and self.state.PLAYERS[0].score < 21:
      _input = input("Enter 'h' to hit or 's' to stand: ")
      match _input:
        case "h":
          logging.debug("Player hits.")
          self.state.hit(self.state.PLAYERS[0])
          self.state.PLAYERS[0].print_hand()
        case "s":
          logging.debug("Player stands.")
        case _:
          logging.info("Invalid input. Please enter 'h' or 's'.")
      logging.info("------------------")
      sleep(1)

    self.state.close()
    self.state.DEALER.print_hand()
    logging.info("------------------")
    WINNERS = self.state.determine_best_hands()
    logging.info(self.state.winning_hands_to_string(WINNERS))
