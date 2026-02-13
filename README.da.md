# Blackjack
Basalt blackjack spil implementeret i Python 3.

For at køre spillet, brug `uv`:
```sh
uv venv
source .venv/bin/activate
uv pip install -r pyproject.toml
python -m src --cli
```

## Demo

![Demo-optagelse](./assets/demo.gif)

## Features
- Blanding af kort
- Uddeling af kort efter typisk Blackjack tilgang
- Spiller-input m.h.t. hit/stand
- Scoring af spillerens og dealerens hånd, win/lose logik

### "Nice-to-have"
- Tracking af wins/losses
- Valg af input I stedet for almindelig indtastning, eg. PyInquirer
  - Mere detaljeret Terminal UI
  - GUI vha. Tkinter, PyQt, eller PyGObject
  - WebUI vha. eg. Flask
- Fremvisning af kort så de er mere tydelige end eg. ♠9
- Online Multiplayer
  - OCI-container image
