import logging

from .view.view import Interface, View


def main(args: list[str] | None = None):
  GUI: View
  if args is None:
    import sys

    args = sys.argv[1:]
  logging.basicConfig(level=logging.INFO, format="%(message)s")
  logging.debug("Arguments: %s", ", ".join(args))
  match args:
    case ["--cli"]:
      GUI = View(Interface.CONSOLE)
    case ["--gui"]:
      GUI = View(Interface.GUI)
    case ["--web"]:
      GUI = View(Interface.WEB)
    case _:
      logging.error(f"Launch arguments are {'invalid' if len(args) else 'missing'}")
      logging.error("Please launch with '--cli', '--gui' or '--web'.")
      return 1
  GUI.display()


if __name__ == "__main__":
  main()
