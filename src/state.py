# The current game state, eg. current deck, hands at play, etc.
from src.logic import card, get_deck


class player:
  ID: int
  HAND: list[card]
  SCORE: int

  def __init__(self, id: int) -> None:
    self.ID = id
    self.HAND = []
    self.SCORE = 0

  # TODO: Fix edge-case of having three Aces on hand
  # TODO: Implement observer pattern
  def update_score(self) -> None:
    self.SCORE = 0
    for _card in sorted(self.HAND, reverse=True):
      print(f"{self.SCORE} before {_card}")
      match _card.rank.value:
        case n if n == 1:
          self.SCORE += 11 if self.SCORE <= 10 else 1
        case n:
          self.SCORE += min(max(n, 1), 10)
      print(f"{self.SCORE} after {_card}")


class game_state:
  DECK: list[card] = []
  DEALER = player(-1)
  PLAYERS: list[player] = []

  def __init__(self, player_count: int = 1) -> None:
    self.DECK = get_deck(number_of_decks=6)
    self.PLAYERS = [player(i) for i in range(1, player_count + 1)]

  def deal_cards(self) -> None:
    self.DEALER.HAND.append(self.DECK.pop())
    for p in self.PLAYERS:
      for _ in range(2):
        p.HAND.append(self.DECK.pop())

  def hit(self, player: player) -> None:
    player.HAND.append(self.DECK.pop())
    player.update_score()

  def close(self) -> None:
    while self.DEALER.SCORE < 17:
      self.DEALER.HAND.append(self.DECK.pop())
      self.DEALER.update_score()

  def determine_best_hands(self) -> list[player]:
    ALL_HANDS = [h for h in [self.DEALER] + self.PLAYERS if h.SCORE <= 21]
    ALL_HANDS.sort(key=lambda x: x.SCORE, reverse=True)
    return [h for h in ALL_HANDS if h.SCORE == ALL_HANDS[0].SCORE]

  def winning_hands_to_str(self, players: list[player]) -> str:
    WINNING_PLAYERS: list = [p for p in enumerate(self.PLAYERS) if p in players]
    print(f"Dealer score: {self.DEALER.SCORE}")
    print(f"Player 1 score: {self.PLAYERS[0].SCORE}")
    if len(WINNING_PLAYERS) == 0:
      return "House wins!"
    if self.DEALER.SCORE == WINNING_PLAYERS[0].SCORE:
      return f"Push, player {', '.join(p.ID for p in WINNING_PLAYERS)} splits!"
    return f"Player {', '.join(p.ID for p in WINNING_PLAYERS)} wins!"
