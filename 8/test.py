import unittest

from main import get_key_values,get_steps

class TestHands(unittest.TestCase):

    def test_type_value(self):
        key , values = get_key_values('AAA = (BBB, CCC)')
        self.assertEqual(key, "AAA", "key")
        self.assertEqual(values['R'], "CCC", "Right")
        self.assertEqual(values['L'], "BBB", "Right")
    def test_get_step(self):
        steps = get_steps("LRL")
        self.assertEqual(steps, ["L","R","L"], "steps")
if __name__ == '__main__':
    unittest.main()