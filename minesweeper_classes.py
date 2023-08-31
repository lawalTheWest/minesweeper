#!/usr/bin/python3

import random


class Cell:
    def __init__(self):
        self.is_mine = False
        # Indicates whether the cell contains a mine.

        self.is_flagged = False
        # Indicates whether the cell has been flagged by the player.

        self.is_revealed = False
        # Indicates whether the cell has been revealed.

        self.adjacent_mines = 0
        # Number of adjacent cells containing mines.

    def reveal(self):
        # Reveals the content of the cell.
        self.is_revealed = True

    def toggle_flag(self):
        # Toggles the flagged state of the cell.
        self.is_flagged = not self.is_flagged

    def set_adjacent_mines(self, counter):
        # Calculates and sets the number of adjacent mines.
        self.adjacent_mines = counter

class Board:
    def __init__(self, num_rows, num_cols, num_mines):
        self.num_rows = num_rows
        # Number of rows on the board.
        
        self.num_cols = num_cols
        # Number of columns on the board.
        
        self.num_mines = num_mines
        # Number of mines on the board.

        '''
            progressive work
            Create a nested list with column and cell number.
            Iterate col number times and 
            create a new Cell object for each iteration.
            The use of an underscore _ as the variable name
            indicates that the variable is not going to
            be used within the loop.
        '''

        self.cells = [[cells() for _ in range(num_cols)] for _ in range(num_rows)]
        # A 2D list of Cell objects representing the game grid.

    def initialize_board(self):
        # Initializes the board with empty cells.
        self.place_mines()
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.set_adjacent_mines(row, col)

    def place_mines(self):
        # Randomly places mines on the board.
        # create a range from 0 to the last cell number
        # select randomly from our range
        # passing the number of mines
        pos_of_mine = random.sample(range(self.num_rows * self.num_cols), self.num_mines)

    def reveal_cell(self):
        # Reveals a cell and handles adjacent empty cells.

    def flag_cell(self):
        # Flags or unflags a cell.

    def is_game_over(self):
        # Checks if the game is over (win or loss).

class Game:
    def __init__(self, board, game_over, win):
        self.board = board
        '''
            Purpose:
                The board attribute represents the game board
                on which the Minesweeper game is played.
                It holds all the information about
                the state of the cells,
                their positions,
                mines,
                flags, and
                revealed cells.
        '''

        self.game_over = game_over
        # Indicates whether the game is over.
        
        self.win = win
        # Indicates whether the player has won.

    def start_game():
        '''
            Initializes the game by
            creating the board and placing mines.
        '''
    def play():
        '''
            Handles player moves,
            updates the board, and
            checks for game status.
        '''
    def check_win():
        '''
            Checks if the player has won by
            revealing all non-mine cells.
        '''
    def end_game():
        '''
            Ends the game by 
            revealing all cells and
            displaying the result.
        '''
class UserInterface:
    # This class handles user input and display.
    def get_user_input():
        # Gets user input for cell selection or action.
    def display_board():
        '''
            Displays the current state of the board
            to the player.
        '''

class main:
    '''
        Game Entry point.
        Purpose:
            Initializes the necessary game objects and
            starts the game loop.
    '''
