# 3D TicTacToe

A strategic extension of the classic TicTacToe game, implemented in Python with Pygame.

Instead of playing on one 3×3 board, **each of the 9 fields contains another 3×3 TicTacToe board**. Your move determines where your opponent has to play next. Select your move wisely to win one the main board!

## 🎮 How to Play

The game consists of a **main board** containing 9 smaller TicTacToe boards.

1. **X starts** and can play anywhere.
2. The position of your move inside a sub-board determines the **sub-board your opponent must play in**.
3. Win a sub-board by getting **3 in a row**. The won sub-board is then marked with your symbol and can no longer be played in.
4. Win the **main board** by winning 3 sub-boards in a row.

### Example
1. X plays in the **top-left** position of the middle sub-board. O must play in the **top-left sub-board** of the main board in the next move.
2. In the next move, O plays in the **middle-right** position of the top-left sub-board. X must play in the **middle-right sub-board** of the main board in the next move.

<div style="display: flex; justify-content: center; gap: 20px;">
  <div style="text-align: center;">
    <strong>First move</strong><br>
    <img width="400" height="452" alt="First move" src="https://github.com/user-attachments/assets/c415b8b8-2bd1-45a9-b323-37536a6e8b71" />
  </div>

  <div style="text-align: center;">
    <strong>Second move</strong><br>
    <img width="400" height="452" alt="Second move" src="https://github.com/user-attachments/assets/c0ad58d6-d57d-483a-a92a-a5b406241766" />
  </div>
</div>

### 🔀 What if the next sub-board is already won?

Two rule variants can be selected before starting:

- **Remain in Square** — Stay in the current active sub-board if your move would direct the opponent to an already won board. If that move also wins the current sub-board, the next player can choose any remaining sub-board.
- **Free Choice** — If your move directs the opponent to an already won sub-board, they can freely choose any remaining sub-board.

## 🕹️ Game Modes

### Players

Choose between:

- **Player vs Player**
- **Player vs Computer**
- **Computer vs Player**
- **Computer vs Computer**

### Visibility

When playing with a human player, choose between:

- **Normal Mode** — The entire board is visible at any time.
- **Memory Mode** — Only the currently active sub-board and the sub-board containing the previous move are visible.

Memory Mode adds an additional challenge by requiring players to remember the state of the hidden boards.

### 🤖 Computer Difficulty

The computer uses a **Minimax algorithm** to determine its moves.

There are **8 difficulty levels**, which control the depth of the search tree and therefore the strength of the computer.

## 🖥️ UI

- 🔴 **Red** — Indicates the active sub-board.
- 🟥 **Light red** — Shows which sub-board would become active if the hovered move were played.
- **Hovering over a field** previews your X or O.
- **Won sub-boards** can be clicked to switch between displaying the large X/O and the actual sub-board configuration.

## 💡 What I Learned

- Designing a new game based on the classic TicTacToe concept
- Building an interactive game UI with **Pygame**
- Implementing a **Minimax algorithm** for computer-controlled players
- Designing different game modes and rule variants
