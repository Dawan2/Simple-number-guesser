# Number Guessing Game

Welcome to the Number Guessing Game, a Python script that challenges you to guess a randomly generated number within a specified range. Test your intuition and see how quickly you can identify the correct number!

## How to Play

1. **Initialization:**
   - The script starts by generating a random number between 1 and 1000.

2. **User Interaction:**
   - You are prompted to pick a number within the given range (initially 1-1000).

3. **Guessing:**
   - Based on your input, the game provides feedback on whether your guess is too high, too low, or correct.

4. **Feedback:**
   - If your guess is correct, the game congratulates you, revealing the number and the number of tries it took.

5. **Adjusting Range:**
   - If your guess is too high or too low, the script adjusts the range accordingly, narrowing down the possible values.

6. **Input Validation:**
   - The script handles various input scenarios, providing feedback for incorrect inputs or interruptions.

7. **Game Termination:**
   - The game ends when you correctly guess the number.

## Usage Example

```plaintext
PICK A NUMBER 1-1000: 500
TOO LOW

PICK A NUMBER 501-1000: 750
TOO HIGH

PICK A NUMBER 501-749: 600
TOO HIGH

PICK A NUMBER 501-599: 550
TOO LOW

PICK A NUMBER 551-599: 575
TOO HIGH

PICK A NUMBER 551-574: 560
TOO LOW

PICK A NUMBER 561-574: 565
TOO LOW

PICK A NUMBER 566-574: 570
TOO LOW

PICK A NUMBER 571-574: 573
TOO HIGH

PICK A NUMBER 571-572: 571
YOU WON! YOU GUESSED 571 IN 9 TRIES!
