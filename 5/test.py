import unittest
from main import Mapper, Mapping, Range_Mapper, RangeIter, parse_seeds, parse_header, parse_seeds_pairs, parse_value

class TestSum(unittest.TestCase):

    def test_seed(self):
        actual = parse_seeds('seeds: 79 14 55 13')
        expected = [79,14,55,13]
        self.assertEqual(actual, expected, "Should parse seeds")
    def test_ranges(self):
        r1 = RangeIter(2,3)
        r2 = RangeIter(1,4)
        actual, remaining = r1.intersection(r2)
        expected = [RangeIter(2,3)]
        self.assertEqual(actual, expected, "Should find intersection")
        expected = [RangeIter(1,2),RangeIter(3,4)]
        self.assertEqual(remaining, expected, "Should find remaining")
    def test_parse_seeds_pairs(self):
        values = parse_seeds_pairs('seeds: 79 14 55 13')
        actual = values
        expected = [RangeIter(79,93),RangeIter(55,68)]
        self.assertEqual(actual, expected, "Should parse seeds")

if __name__ == '__main__':
    unittest.main()