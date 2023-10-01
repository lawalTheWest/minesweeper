#!/usr/bin/python3
'''
    The Minesweeper functionalities
'''
import random
import pygame

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


        self.cells = [[Cell() for _ in range(num_cols)] for _ in range(num_rows)]
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
        for pos in pos_of_mine:
            row = pos // self.num_cols
            col = pos % self.num_cols
            self.cells[row][col].is_mine = True

    def set_adjacent_mines(self, row, col):
        # Calculates and sets the number of adjacent mines.
        pass 

    def reveal_adjacent_cells(self, row, col):
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue  # Skip the current cell
                r, c = row + dr, col + dc
                if 0 <= r < self.num_rows and 0 <= c < self.num_cols:
                    adjacent_cell = self.cells[r][c]
                    if not adjacent_cell.is_revealed and not adjacent_cell.is_flagged:
                        adjacent_cell.reveal()
                        if adjacent_cell.adjacent_mines == 0:
                            self.reveal_adjacent_cells(r, c)

    def reveal_cell(self, row, col):
        # Reveals a cell and handles adjacent empty cells.
        if 0 <= row < self.num_rows and 0 <= col < self.num_cols:
            cell = self.cells[row][col]
            if not cell.is_revealed and not cell.is_flagged:
                cell.reveal()
                if cell.is_mine:
                    return False
                    # To end the game if one steps on the mine
                elif cell.adjacent_mines == 0:
                    self.reveal_adjacent_cells(row, col)
            return True # game on to continue

    def flag_cell(self, row, col):
        # Flags or unflags a cell.
        if self.num_rows > row >= 0 and self.num_cols > col >= 0:
            cell = self.cells[row][col]
            if not cell_is_revealed:
                cell.toggle_flag

    def display_board(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell = self.cells[row][col]
                if cell.is_revealed:
                    if cell.is_mine:
                        print("X", end=" ")  # Display mines as "X"
                    else:
                        print(cell.adjacent_mines, end=" ")
                elif cell.is_flagged:
                    print("F", end=" ")  # Display flagged cells as "F"
                else:
                    print(".", end=" ")  # Display unrevealed cells as "."
            print()  # Move to the next row

    def is_game_over(self):
        # Checks if the game is over (win or loss).
        pass

class Game:
    def __init__(self, board):
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

        self.game_over = False
        # Indicates whether the game is over.
        
        self.win = False
        # Indicates whether the player has won.

    def start_game(self):
        '''
            Initializes the game by
            creating the board and placing mines.
        '''
        self.board.initialize_board()

    def play(self):
        '''
            Handles player moves,
            updates the board, and
            checks for game status.
            this includes the,
            placing flags and the steps.
        '''
        while not self.game_over:
            self.board.display_board()
            row, col = UserInterface.get_user_input(self.board)
            result = self.board.reveal_cell(row, col)
            if not result:
                self.game_over = True
            else:
                self.check_win()

    def check_win(self):
        '''
            Checks if the player has won by
            revealing all non-mine cells.
        '''
        pass

    def end_game(self):
        '''
            Ends the game by 
            revealing all cells and
            displaying the result.
        '''
        pass

class UserInterface:
    # This class handles user input and display.
    @staticmethod
    def get_user_input(board):
        while True:
            try:
                row = int(input("Enter the row (0 to {}): ".format(board.num_rows - 1)))
                col = int(input("Enter the column (0 to {}): ".format(board.num_cols - 1)))
                if 0 <= row < board.num_rows and 0 <= col < board.num_cols:
                    return row, col
                else:
                    print("Invalid row or column. Please enter values within the valid range.")
            except ValueError:
                print("Invalid input. Please enter valid integer values for row and column.")

    '''
    def get_user_input():
        # Gets user input for cell selection or action.
        try:
            row = int(input("Enter the row: "))
            col = int(input("Enter the column: "))
            return row, col
        except ValueError:
            print("Invalid input. Please enter valid row and column numbers.")
            return UserInterface.get_user_input()
    '''

    '''
    def display_board():
        ''
            Displays the current state of the board
            to the player.
    '''
    @staticmethod
    def display_board(board):
        for row in range(board.num_rows):
            for col in range(board.num_cols):
                cell = board.cells[row][col]
                if cell.is_revealed:
                    if cell.is_mine:
                        print("X", end=" ")  # Display mines as "X"
                    else:
                        print(cell.adjacent_mines, end=" ")
                elif cell.is_flagged:
                    print("F", end=" ")  # Display flagged cells as "F"
                else:
                    print(".", end=" ")  # Display unrevealed cells as "."
            print()  # Move to the next row

if __name__ == '__main__':
    '''
        Game Entry point.
        Purpose:
            Initializes the necessary game objects and
            starts the game loop.
    '''
    num_rows = 5
    num_cols = 5
    num_mines = 3

    board = Board(num_rows, num_cols, num_mines)
    game = Game(board)

    game.start_game()
    
    while not game.game_over:
        UserInterface.display_board(board)
        row, col = UserInterface.get_user_input(board)
        game.play()
    '''
    game.play()
    '''
    game.end_game()

    #Initialize Pygame
    pygame.init()

    # Set up the window
    screen_width = 400
    screen_height = 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Minesweeper")

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
