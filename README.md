# 3D-TicTacToe
I created a fun interactive game using Pygame. One can play against a friend or against the computer.

## Requirements
Python 3.13
Pygame 2.6.1

## Rules of the game
The game consists of a large standard TicTacToe board (the main board), where each of the 9 fields in it contains itself a smaller TicTacToe sub board. The starting player ("X") can place his first token in any field of any sub board. The location where he placed his token inside a sub board determines in which sub-board his opponent ("O") is allowed to place his next token: If player X placed his token at position A ("top-right", "top-middle", "bottom-left", ...) inside a particular sub board, then player O is allowed to place his next token inside the sub board located at that position A ("top-right", "top-middle", "bottom-left", ...) inside the main board. **Example:** Player X places his first token in the _top-left_ corner of the sub board located in the middle of the main board. Then player O can place his next token in any field inside the sub board located at the _top-left_ corner of the main board.
