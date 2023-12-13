import unittest

from main import next_history,back_history

class TestHands(unittest.TestCase):
    def test_next_history(self):
        next = next_history([1,2,3])
        self.assertEqual(next, 4 , "next in history")
    def test_next_step(self):
        next = next_history([1,3,5,7])
        self.assertEqual(next, 9 , "next in history")
    def test_back_step(self):
        next = back_history([10,13,16,21,30,45])
        self.assertEqual(next, 5 , "next in history")
if __name__ == '__main__':
    unittest.main()