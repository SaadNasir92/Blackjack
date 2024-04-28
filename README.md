# Novice Blackjack Game in Python

## Description
This project is a simple command-line Blackjack game implemented in Python. It allows players to experience a classic blackjack game against a virtual dealer, with features including card dealing, hand evaluations, betting, and decision-making (hit or stay).

## Features
- **Gameplay Interaction**: Engage in blackjack directly from the command line with intuitive prompts.
- **Dynamic Betting System**: Start with a virtual chip stack and make bets on each hand.
- **Automatic Hand Evaluation**: Hands are automatically evaluated with adjustments for Aces being either 1 or 11, depending on the situation.
- **Win/Loss Calculation**: Outcomes of games are determined based on standard Blackjack rules.

## Technologies Used
- **Python**: Main programming language used.
- **Random**: Python module utilized for card dealing.
- **Art**: Module used to incorporate custom ASCII art for an enhanced game presentation.

## How to Run the Game
1. Clone the repository to your local machine:
   ```bash
   git clone [https://github.com/SaadNasir92/Blackjack]

2. Make sure Python is installed on your machine. If not, download and install it from python.org.

3. Navigate to the directory containing the game files and run the following command in the terminal:
   ```bash
    python blackjack.py

4. Follow the on-screen prompts to play the game.

## Code Example
```python
def deal_cards(deck):
    """Deals cards. Returns a random list representing a hand."""
    hand = []
    cards = list(deck.keys())
    for _ in range(2):
        hand.append(random.choice(cards))
    return hand
```
##  Lessons Learned
This project enhanced my understanding of Python programming, particularly in using control structures, functions, and managing state. It was an excellent exercise in applying theoretical knowledge in a practical, fun application.

## Future Improvements
- User Interface: Implement a graphical user interface (GUI) to improve user interaction.
- Multiplayer Functionality: Add features to play against other players online.
- Advanced Betting Strategies: Introduce more complex betting strategies and variations of Blackjack rules.