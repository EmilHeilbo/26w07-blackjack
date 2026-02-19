# Blackjack
A game of blackjack implemented in Python 3

To run the game, use `uv`:
```sh
uv sync --no-dev
uv run -m blackjack
```

## Demo

![Demo recording](./assets/demo.gif)

## Features
- Shuffling cards
- Dealing cards according to typical Blackjack approach
- Player input for hit/stand
- Scoring of player's and dealer's hand, win/lose logic

### "Nice-to-have"
- Staking / betting system
- Tracking of wins/losses
- Choice of input instead of regular input
  - More detailed Terminal UI
  - Graphical UI
  - WebUI
- Clearer displaying of cards
- Online Multiplayer
  - OCI-container image

Playing card assets are from [Google Code Archive](https://code.google.com/archive/p/vector-playing-cards/)
