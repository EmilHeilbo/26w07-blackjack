import logging
from enum import Enum

from ..state import Game_State
from . import console

Interface = Enum("Interface", ["CONSOLE", "GUI", "WEB"])


class View:
  """Represents the view of the game, responsible for displaying the game state to the user."""

  state: Game_State
  INTERFACE: Interface

  def __init__(self, interface: Interface, state: Game_State = Game_State()):
    self.state = state
    self.INTERFACE = interface

  def display(self):
    match self.INTERFACE:
      case Interface.CONSOLE:
        logging.info("Opening console interface...")
        view = console.ConsoleView(self.state)
        view.run()
        return 0
