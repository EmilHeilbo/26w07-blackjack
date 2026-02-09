from src import logic


def test_correct_deck_size():
  assert len(logic.get_deck(3)) == 52 * 3
  assert len(logic.get_deck()) == 52


def test_ensure_shuffle_works():
  assert logic.get_deck(shuffle_deck=False) != logic.get_deck()
