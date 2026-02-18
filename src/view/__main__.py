import logging
from sys import argv, exit

from .console import ConsoleView


def main(args: list[str]):
  LAUNCH_ARGS = ["--cli", "--gui", "--web"]
  interface: ConsoleView | None

  logging.basicConfig(level=logging.INFO, format="%(message)s")
  logging.debug("Arguments: %s", ", ".join(args))
  _matches = 0
  for arg in LAUNCH_ARGS:
    if arg in args:
      _matches += 1
  if _matches > 1:
    logging.error(f"Multiple launch arguments found: {args}")
    logging.error("Please launch with only one of '--cli', '--gui' or '--web'.")
    exit(1)
  match args:
    case _ if LAUNCH_ARGS[0] in args:
      interface = ConsoleView()
    case _ if LAUNCH_ARGS[1] in args:
      logging.error("GUI interface is not implemented yet.")
      exit(1)
    case _ if LAUNCH_ARGS[2] in args:
      logging.error("Web interface is not implemented yet.")
      exit(1)
    case _:
      logging.error(f"Launch arguments are {'invalid' if len(args) else 'missing'}")
      logging.error("Please launch with '--cli', '--gui' or '--web'.")
      exit(1)
  interface.run()
  exit(0)


if __name__ == "__main__":
  main(argv[1:])
