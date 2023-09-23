# Minesweeper Python Implementation Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Cell Class](#cell-class)
3. [Board Class](#board-class)
4. [Game Class](#game-class)
5. [UserInterface Class](#userinterface-class)
6. [Usage](#usage)
7. [Pygame Integration](#pygame-integration)
8. [Conclusion](#conclusion)

## 1. Introduction <a name="introduction"></a>

This Minesweeper Python implementation provides a comprehesive and modular approach to creating both a text-based and graphical version of the Minesweeper game.
TheMinesweeper is a classic single-player puzzle game where the player's objective is to uncover all cells on the game board that do not contain mines.

This documentation covers the key components of the codebase, including:
- classes,
- methods, and their
- functionalities.

## 2. Cell Class <a name="cell-class"></a>

The `Cell` class represents individual cells on the Minesweeper board. Each cell has the following attributes:

- `is_mine`: Indicates whether the cell contains a mine.
- `is_flagged`: Indicates whether the cell has been flagged by the player.
- `is_revealed`: Indicates whether the cell has been revealed.
- `adjacent_mines`: Number of adjacent cells containing mines.

### Methods:
- `reveal()`: Reveals the content of the cell.
- `toggle_flag()`: Toggles the flagged state of the cell.
- `set_adjacent_mines(counter)`: Calculates and sets the number of adjacent mines.

## 3. Board Class <a name="board-class"></a>

The `Board` class represents the game board in Minesweeper.
- It initializes the board with empty cells,
- randomly places mines, and
- sets the number of adjacent mines for each cell.

### Key Attributes:
- `num_rows`: Number of rows on the board.
- `num_cols`: Number of columns on the board.
- `num_mines`: Number of mines on the board.
- `cells`: A 2D list of `Cell` objects representing the game grid.

### Methods:
- `initialize_board()`: Initializes the board with empty cells, places mines, and sets adjacent mines.
- `place_mines()`: Randomly places mines on the board.
- `set_adjacent_mines(row, col)`: Calculates and sets the number of adjacent mines for a given cell.
- `reveal_adjacent_cells(row, col)`: Reveals adjacent cells when an empty cell is revealed.
- `reveal_cell(row, col)`: Reveals a cell, handles adjacent empty cells, and checks for mines or game over.
- `flag_cell(row, col)`: Flags or unflags a cell.
- `display_board()`: Displays the current state of the board to the player.
- `is_game_over()`: Checks if the game is over, either by win or loss.

## 4. Game Class <a name="game-class"></a>

The `Game` class manages the gameplay.
- It tracks the game state, including whether the game is over or if the player has won.

### Key Attributes:
- `board`: An instance of the `Board` class representing the game board.
- `game_over`: Indicates whether the game is over.
- `win`: Indicates whether the player has won.

### Methods:
- `start_game()`: Initializes the game by creating the board and placing mines.
- `play()`: Handles player moves, updates the board, and checks for game status, including flagging cells and revealing cells.
- `check_win()`: Checks if the player has won by revealing all non-mine cells.
- `end_game()`: Ends the game by revealing all cells and displaying the result.

## 5. UserInterface Class <a name="userinterface-class"></a>

The `UserInterface` class handles user input and display. It contains static methods for getting user input and displaying the board.

### Key Methods:
- `get_user_input(board)`: Gets valid user input for row and column within the board's dimensions.
- `display_board(board)`: Displays the current state of the board to the player.

## 6. Usage <a name="usage"></a>

To use the Minesweeper game, create instances of the `Board` and `Game` classes, and then call the relevant methods to play the game. You can use the `UserInterface` class to handle user input and display the board.

## 7. Pygame Integration <a name="pygame-integration"></a>

The code also includes integration with the Pygame library to create a graphical interface for the Minesweeper game (This part is still undrr intergration). It utilizes Pygame to display the game board, cells, and interactions within a graphical window.

Key Pygame-related code elements include initializing Pygame, creating a Pygame window, and updating the window based on the game state within the game loop.

## 8. Conclusion <a name="conclusion"></a>

No conclusion yet
