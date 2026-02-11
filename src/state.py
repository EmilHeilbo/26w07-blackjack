# The current game state, eg. current deck, hands at play, etc.
from src.logic import Card, get_deck


class Player:
  id: int
  hand: list[Card]
  score: int

  def __init__(self, id: int) -> None:
    self.id = id
    self.hand = []
    self.score = 0

  # TODO: Fix edge-case of having three Aces on hand
  # TODO: Implement observer pattern
  def update_score(self) -> None:
    self.score = 0
    for _card in sorted(self.hand, reverse=True):
      print(f"{self.score} before {_card}")
      match _card.rank.value:
        case n if n == 1:
          self.score += 11 if self.score <= 10 else 1
        case n:
          self.score += min(max(n, 1), 10)
      print(f"{self.score} after {_card}")

  def print_hand(self) -> None:
    name = "Dealer" if self.id == 0 else f"Player {self.id}"
    print(f"""
      {name} hand: {", ".join([str(c) for c in self.hand])}
      {name} score: {self.score}
      """)


class Game_State:
  deck: list[Card] = []
  DEALER: Player
  PLAYERS: list[Player]

  def __init__(self, player_count: int = 1) -> None:
    self.deck = get_deck(number_of_decks=6)
    self.DEALER = Player(0)
    self.PLAYERS = [Player(i) for i in range(1, player_count + 1)]

  def deal_cards(self) -> None:
    self.DEALER.hand.append(self.deck.pop())
    for _ in range(2):
      for p in self.PLAYERS:
        p.hand.append(self.deck.pop())
    for p in [self.DEALER, *self.PLAYERS]:
      p.update_score()

  def hit(self, player: Player) -> None:
    player.hand.append(self.deck.pop())
    player.update_score()

  def close(self) -> None:
    while self.DEALER.score < 17:
      self.DEALER.hand.append(self.deck.pop())
      self.DEALER.update_score()

  def determine_best_hands(self) -> list[Player]:
    ALL_HANDS = [h for h in [self.DEALER, *self.PLAYERS] if h.score <= 21]
    ALL_HANDS.sort(key=lambda x: x.score, reverse=True)
    return [h for h in ALL_HANDS if h.score == ALL_HANDS[0].score]

  def winning_hands_to_string(self, players: list[Player]) -> str:
    WINNING_PLAYERS: list = [p for p in enumerate(self.PLAYERS) if p in players]
    print(f"Dealer score: {self.DEALER.score}")
    print(f"Player 1 score: {self.PLAYERS[0].score}")
    if len(WINNING_PLAYERS) == 0:
      return "House wins!"
    if self.DEALER.score == WINNING_PLAYERS[0].SCORE:
      return f"Push, player {', '.join(p.ID for p in WINNING_PLAYERS)} splits!"
    return f"Player {', '.join(p.ID for p in WINNING_PLAYERS)} wins!"
