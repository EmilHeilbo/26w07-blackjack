# Blackjack
Et blackjack spil implementeret i Python 3

For at køre spillet, brug `uv`:
```sh
uv venv
source .venv/bin/activate
uv pip install -r pyproject.toml
python -m view --cli
```

## Demo

![Demo-optagelse](./assets/demo.gif)

## Features
- Blanding af kort
- Uddeling af kort efter typisk Blackjack tilgang
- Spiller-input m.h.t. hit/stand
- Scoring af spillerens og dealerens hånd, win/lose logik

### "Nice-to-have"
- Staking / betting system
- Tracking af wins/losses
- Valg af input I stedet for almindelig indtastning
  - Mere detaljeret Terminal brugergrænseflade
  - Grafisk brugergrænseflade
  - WebUI
- Mere tydelig fremvisning af kort 
- Online Multiplayer
  - OCI-container image

Spillekort assets stammer fra [Google Code Archive](https://code.google.com/archive/p/vector-playing-cards/)
