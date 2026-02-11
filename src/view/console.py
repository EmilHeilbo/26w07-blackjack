from src.state import Game_State


class ConsoleView(Game_State):
  STATE: Game_State

  def __init__(self, state):
    self.state = state

  def run(self):
    _intro_text = """
    Welcome to Blackjack!
    Rules:
      - The goal is to get as close to 21 as possible without going over.
      - You can hit (take another card) or stand (keep your current hand).
      - The dealer hits until they reach 17 or higher.
      - The game stands automatically when the player's score is 21 or higher.

      ------------------
    """
    print(_intro_text)
    self.state.deal_cards()
    for p in [self.state.DEALER, *self.state.PLAYERS]:
      p.print_hand()

    _input = None
    while _input != "s" and self.state.PLAYERS[0].score < 21:
      _input = input("Enter 'h' to hit or 's' to stand: ")
      match _input:
        case "h":
          self.state.hit(self.state.PLAYERS[0])
          print(
            f"Player hand: {self.state.PLAYERS[0].hand}, score: {self.state.PLAYERS[0].score}"
          )
        case "s":
          print("Player stands.")
          self.state.close()
          self.state.DEALER.print_hand()
          self.state.winning_hands_to_string(self.state.determine_best_hands())

        case _:
          print("Invalid input. Please enter 'h' or 's'.")
