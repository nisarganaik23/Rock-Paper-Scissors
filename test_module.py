import unittest
from RPS import player

class TestPlayer(unittest.TestCase):
    def test_player(self):
        # Test that player returns a valid move
        valid_moves = ["R", "P", "S"]
        self.assertIn(player("R"), valid_moves)
        self.assertIn(player("P"), valid_moves)
        self.assertIn(player("S"), valid_moves)

if __name__ == "__main__":
    unittest.main()
