# 3D TicTacToe

A strategic extension of the classic TicTacToe game, implemented in Python with Pygame.

Instead of playing on one 3×3 board, **each of the 9 fields contains another 3×3 TicTacToe board**. Your move determines where your opponent has to play next. Select your move wisely to win the main board!

## 🎮 How to Play

The game consists of a **main board** containing 9 smaller TicTacToe boards.

1. **X starts** and can play anywhere.
2. The position of your move inside a sub-board determines the **sub-board your opponent must play in**.
3. Win a sub-board by getting **3 in a row**. The won sub-board is then marked with your symbol and can no longer be played in.
4. Win the **main board** by winning 3 sub-boards in a row.

### Example
1. X plays in the **top-left** position of the middle sub-board. O must play in the **top-left sub-board** of the main board in the next move.
2. In the next move, O plays in the **middle-right** position of the top-left sub-board. X must play in the **middle-right sub-board** of the main board in the next move.

<table>
  <tr>
    <td align="center">
      <strong>First move</strong><br>
      <img width="400" height="452" alt="First move" src="https://github.com/user-attachments/assets/c415b8b8-2bd1-45a9-b323-37536a6e8b71" />
    </td>
    <td align="center">
      <strong>Second move</strong><br>
      <img width="400" height="452" alt="Second move" src="https://github.com/user-attachments/assets/c0ad58d6-d57d-483a-a92a-a5b406241766" />
    </td>
  </tr>
</table>

### 🔀 What if the next sub-board is already won?

Two rule variants can be selected before starting:

- **Remain in Square:** Stay in the current active sub-board if your move would direct the opponent to an already won board. If that move also wins the current sub-board, the next player can choose any remaining sub-board.
- **Free Choice:** If your move directs the opponent to an already won sub-board, they can freely choose any remaining sub-board.

<table>
  <tr>
    <td align="center">
      <strong>Remain in Square</strong><br>
      <img width="400" height="452" alt="Bildschirmfoto 2026-08-12 um 14 14 10" src="https://github.com/user-attachments/assets/a7262d47-55ca-4476-a23a-ae93abc962ca" />
    </td>
    <td align="center">
      <strong>Free Choice</strong><br>
      <img width="400" height="452" alt="Bildschirmfoto 2026-08-12 um 14 14 41" src="https://github.com/user-attachments/assets/fb2ddaae-84c4-4bef-8a5b-88119779f9b0" />
    </td>
  </tr>
</table>

## 🕹️ Game Modes

### Players

Choose between:

- **Player vs Player**
- **Player vs Computer**
- **Computer vs Player**
- **Computer vs Computer**

### Visibility

When playing with a human player, choose between:

- **Normal Mode:** The entire board is visible at any time.
- **Memory Mode:** Only the currently active sub-board and the sub-board containing the previous move are visible.

Memory Mode adds an additional challenge by requiring players to remember the state of the hidden boards.

<table>
  <tr>
    <td align="center">
      <strong>Normal Mode</strong><br>
      <img width="400" height="452" alt="Bildschirmfoto 2026-08-12 um 14 19 31" src="https://github.com/user-attachments/assets/3c589692-cce2-474f-a8b4-15460042ffe6" />
    </td>
    <td align="center">
      <strong>Memory Mode</strong><br>
      <img width="400" height="452" alt="Bildschirmfoto 2026-08-12 um 14 21 34" src="https://github.com/user-attachments/assets/338a3029-3840-4041-806d-c7ece6481720" />
    </td>
  </tr>
</table>

### 🤖 Computer Difficulty

The computer uses a **Minimax algorithm** to determine its moves.

There are **8 difficulty levels**, which control the depth of the search tree and therefore the strength of the computer.

## 🖥️ UI

- Playable sub-boards are marked red.
- Hovering over a field previews your X or O and marks the sub-boards which become playable in the next turn by light-red.
- Won sub-boards can be clicked to switch between displaying the large X/O and the actual sub-board configuration.

<table>
  <tr>
    <td align="center">
      <strong>Show big tokens (default)</strong><br>
      <img width="400" height="452" alt="Bildschirmfoto 2026-08-12 um 14 30 36" src="https://github.com/user-attachments/assets/ff834686-8950-4de9-b77c-f8bc22e2fa7b" />
    </td>
    <td align="center">
      <strong>Show won board configuration</strong><br>
      <img width="400" height="452" alt="Bildschirmfoto 2026-08-12 um 14 30 58" src="https://github.com/user-attachments/assets/2ed57467-c873-4712-9bf0-30bff042222f" />
    </td>
  </tr>
</table>
