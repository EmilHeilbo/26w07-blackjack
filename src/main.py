import logging
from sys import argv

from src.view.view import Interface, View


def main(args: list[str]):
  logging.info("Arguments: ", ", ".join(args))
  match args:
    case ["--console"]:
      logging.info("Console mode")
      View(Interface["CONSOLE"])
    case ["--gui"]:
      logging.info("GUI mode")
    case _:
      logging.info("Invalid arguments")


if __name__ == "__main__":
  main(argv)
