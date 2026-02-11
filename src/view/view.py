from enum import Enum

import src.view.console as console
from src.state import Game_State

Interface = Enum("Interface", ["CONSOLE", "GUI", "WEB"])


class View:
  state: Game_State
  INTERFACE: Interface

  def __init__(self, interface: Interface, state: Game_State = Game_State()):
    self.state = state
    self.INTERFACE = interface

  def display(self):
    match self.INTERFACE:
      case Interface.CONSOLE:
        print("Opening console interface...")
        view = console.ConsoleView(self.state)
        view.run()
        return 0
