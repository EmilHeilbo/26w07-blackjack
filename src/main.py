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
    case ["--console"]:
      logging.debug("Console mode")
      GUI = View(Interface.CONSOLE)

    case ["--gui"]:
      logging.debug("GUI mode")
      GUI = View(Interface.GUI)
    case _:
      logging.error(f"Launch arguments are {'invalid' if len(args) else 'missing'}")
      logging.error("Please launch with either '--console' or '--gui'")
      return 1
  GUI.display()


if __name__ == "__main__":
  main()
