# Blackjack
Basic blackjack game implemented in Python 3

To run the game, use `uv`:
```sh
uv venv
source .venv/bin/activate
uv pip install -r pyproject.toml
python -m src --cli
```

## Features
- Shuffling cards
- Dealing cards according to typical Blackjack approach
- Player input for hit/stand
- Scoring of player's and dealer's hand, win/lose logic

### "Nice-to-have"
- Tracking of wins/losses
- Choice of input instead of regular input, e.g. PyInquirer
  - More detailed Terminal UI
  - GUI using Tkinter, PyQt or PyGObject
  - WebUI using Flask
- Displaying cards so they are more clear than eg. ♠9
- Online Multiplayer
  - OCI-container image
