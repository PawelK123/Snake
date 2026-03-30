# 🐍 Snake Game

A Python clone of the classic Snake game built with the `turtle` module. Eat food to grow longer, avoid the walls and your own tail — and beat your high score!

---

## 📋 Requirements

- Python 3.x
- No external libraries required (uses only the built-in `turtle` module)
- A `data.txt` file to store the high score (created automatically on first save)

---

## 🚀 How to Run

```bash
python main.py
```

---

## 🎮 How to Play

1. The snake starts in the center of a black 600×600 screen
2. Use the **arrow keys** to change direction
3. Eat the **blue dot** to grow longer and earn points
4. Avoid hitting the **walls** or your own **tail** — the snake resets on collision
5. Your high score is saved to `data.txt` and persists between sessions

---

## 🏗️ Code Structure

### `main.py`
Entry point of the game. Sets up the screen, initializes all objects, and runs the main game loop — handling movement, food collision, wall collision, and self-collision.

### `Snake` — `snake.py`

| Method | Description |
|---|---|
| `create_snake()` | Builds the initial 3-segment snake |
| `move()` | Moves each segment forward following the head |
| `up() / down() / left() / right()` | Changes direction (prevents reversing) |
| `extend()` | Adds a new segment at the tail |
| `reset()` | Clears the snake and rebuilds it at the start |

### `Food` — `food.py`

| Method | Description |
|---|---|
| `refresh()` | Moves the food to a random position on the screen |

### `Scoreboard` — `scoreboard.py`

| Method | Description |
|---|---|
| `update_scoreboard()` | Redraws the current score and high score |
| `collision_with_food()` | Increments score by 1 |
| `reset()` | Resets score, saves high score to `data.txt` if beaten |

---


