
import unittest
from main import get_type_value,get_cards_value

class TestHands(unittest.TestCase):

    def test_type_value(self):
        card1 = get_type_value('AAAKK')
        card2 = get_type_value('AAKKK')
        self.assertEqual(card1, card2, "Should same type value")
        card1 = get_type_value('AAAKK')
        card2 = get_type_value('AA1KK')
        self.assertGreater(card1, card2, "Should same type value")
        card1 = get_type_value('AAA32')
        card2 = get_type_value('AA2KK')
        self.assertGreater(card1, card2, "Should same type value")
        card1 = get_type_value('AAAA2')
        card2 = get_type_value('AAAKK')
        self.assertGreater(card1, card2, "Should same type value")
    def test_card_value(self):
        card1 = get_cards_value('AAAKK')
        card2 = get_cards_value('AAKKK')
        self.assertNotEqual(card1, card2, "Should same type value")
        card1 = get_cards_value('AAAKK')
        card2 = get_cards_value('AA2KK')
        self.assertGreater(card1, card2, "Should same type value")
        card1 = get_cards_value('AAJ32')
        card2 = get_cards_value('AA2KK')
        self.assertGreater(card1, card2, "Should same type value")
        card1 = get_cards_value('AAJA2')
        card2 = get_cards_value('AATKK')
        self.assertGreater(card1, card2, "Should same type value")
if __name__ == '__main__':
    unittest.main()