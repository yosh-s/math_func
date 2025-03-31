# MathBot - A Telegram Bot for Mathematical Operations

## Description
MathBot is a Telegram bot that performs basic mathematical operations such as calculating squares, square roots, checking prime numbers, and computing the least common multiple (LCM) and highest common factor (HCF). It also maintains a history of calculations for each user.

## Features
- Calculates the square and square root of a given number.
- Checks whether a number is prime.
- Computes the least common multiple (LCM) of a list of numbers.
- Computes the highest common factor (HCF) of a list of numbers.
- Maintains a history of user queries.
- Provides an interactive inline keyboard for selecting operations.

## Installation & Setup
### Prerequisites
- Python 3.x
- `pyTelegramBotAPI` library

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/MathBot.git
   cd MathBot
   ```
2. Install dependencies:
   ```bash
   pip install pyTelegramBotAPI
   ```
3. Replace `BOT_TOKEN` in `main.py` with your actual Telegram bot token.
4. Run the bot:
   ```bash
   python main.py
   ```

## Commands
- `/start` - Start the bot and display the main menu.
- `/help` - Show a help message explaining the bot's functions.
- `/his` - Show the history of previous calculations.

## Usage
1. Start the bot using `/start`.
2. Choose an operation using the inline keyboard.
3. Enter the required numbers to perform the selected operation.
4. The bot responds with the computed result and logs the calculation in the history.

## Example Interactions
```
User: /start
Bot: Howdy [User Name], how are you doing?
Bot: Choose Option [Square | Square Root | Prime | LCM | HCF]

User: 25 (after selecting Square)
Bot: 625

User: 16 (after selecting Square Root)
Bot: 4.0
```

## License
This project is licensed under the MIT License.

## Author
Yoshmika Sandeepa

## Contributions
Feel free to submit pull requests or report issues if you find any bugs or have suggestions for improvements.

