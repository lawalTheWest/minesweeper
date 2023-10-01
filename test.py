import unittest
from minesweeper_classes import Cell  # Import your Cell class

class TestCell(unittest.TestCase):
    def test_initial_state(self):
        cell = Cell()
        self.assertFalse(cell.is_mine)
        self.assertFalse(cell.is_flagged)
        self.assertFalse(cell.is_revealed)
        self.assertEqual(cell.adjacent_mines, 0)

    def test_reveal(self):
        cell = Cell()
        cell.reveal()
        self.assertTrue(cell.is_revealed)

    def test_toggle_flag(self):
        cell = Cell()
        cell.toggle_flag()
        self.assertTrue(cell.is_flagged)
        cell.toggle_flag()
        self.assertFalse(cell.is_flagged)

    def test_set_adjacent_mines(self):
        cell = Cell()
        cell.adjacent_mines = 3
        self.assertEqual(cell.adjacent_mines, 3)

if __name__ == '__main__':
    unittest.main()

