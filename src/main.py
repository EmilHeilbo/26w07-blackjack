from sys import argv

from src.view.view import Interface, View


def main(args: list[str]):
  print("Arguments: ", ", ".join(args))
  match args:
    case ["--console"]:
      print("Console mode")
      View(Interface["CONSOLE"])
    case ["--gui"]:
      print("GUI mode")
    case _:
      print("Invalid arguments")


if __name__ == "__main__":
  main(argv)
