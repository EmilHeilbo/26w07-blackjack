import logging

from src.state import Game_State

from .view.console import ConsoleView


def main(args: list[str] | None = None):
  INTERFACE: ConsoleView | None
  if args is None:
    import sys

    args = sys.argv[1:]
  logging.basicConfig(level=logging.INFO, format="%(message)s")
  logging.debug("Arguments: %s", ", ".join(args))
  state = Game_State()
  match args:
    case ["--cli"]:
      INTERFACE = ConsoleView(state)
    case ["--gui"]:
      logging.error("GUI interface is not implemented yet.")
      return 1
    case ["--web"]:
      logging.error("Web interface is not implemented yet.")
      return 1
    case _:
      logging.error(f"Launch arguments are {'invalid' if len(args) else 'missing'}")
      logging.error("Please launch with '--cli', '--gui' or '--web'.")
      return 1
  INTERFACE.run()


if __name__ == "__main__":
  main()
