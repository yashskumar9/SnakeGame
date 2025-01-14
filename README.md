
# Snake Game

Welcome to the Snake Game, a classic arcade game implemented in Python using the `turtle` module. The objective of the game is to control the snake, eat the food, and grow in size while avoiding collisions with walls or the snake's own body.
<br>


<p align='center'>
  <a>
    <img src='https://github.com/user-attachments/assets/bccac36b-d735-4870-b9b3-19f55518caa6'>
  </a>
</p>

## Features

- **Responsive Controls**: Use arrow keys to control the snake's movement (Up, Down, Left, Right).
- **Dynamic Gameplay**: Snake grows in size each time it eats the food.
- **Score Tracking**: Keep track of your score as you play.
- **Collision Detection**: Game resets if the snake collides with the walls or itself.
- **Smooth Animations**: Screen updates dynamically to ensure smooth gameplay.
- **Increasing Speed**: The speed of the snake movement will increase as it eats the food.

## How to Play

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yashskumar9/snake-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd snake-game
   ```
3. Ensure you have Python installed. The game requires Python 3.x.

4. Run the game:
   ```bash
   python main.py
   ```
5. Use the following keys to control the snake:
   - **Up Arrow**: Move up
   - **Down Arrow**: Move down
   - **Left Arrow**: Move left
   - **Right Arrow**: Move right

## Project Structure

```
├── main.py           # Entry point of the game
├── snake.py          # Contains the Snake class and its behaviors
├── food.py           # Contains the Food class for generating food on the screen
├── score_board.py    # Contains the ScoreBoard class for tracking and displaying the score
```

## Dependencies

The game relies on Python's built-in `turtle` and `time` modules, so no external libraries are required.

