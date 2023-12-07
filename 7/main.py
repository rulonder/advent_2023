from collections import defaultdict 
tranlate = {"A":13,"K":12,"Q":11,"J":10,"T":9,"9":8,"8":7,"7":6,"6":5,"5":4,"4":3,"3":2,"2":1}
tranlate_joker = {"A":13,"K":12,"Q":11,"J":0,"T":9,"9":8,"8":7,"7":6,"6":5,"5":4,"4":3,"3":2,"2":1}
def get_type_value(hand_0,joker=False):
    sets = defaultdict(int)
    jokers = 0
    hand = hand_0
    if joker:
        hand = hand_0.replace("J","")
        jokers = len(hand_0) - len(hand)
    for card in hand:
        sets[card] += 1
    # add jokers to higest value unless all cards are jokers
    values = sorted(sets.values())
    if jokers == len(hand_0):
        values = [jokers]
    else:
        values[-1] += jokers
    return sum([ 6**x for x in values])
def get_cards_value(hand,translate=tranlate):
    reversed = hand[::-1] 
    return sum([translate[reversed[i]]*14**i for i in range(len(reversed))])
class Hand(object):
    def __init__(self,hand,bet,translate=tranlate, joker=False):
        self.hand = hand
        self.bet = int(bet)
        self.value = get_type_value(hand,joker)*14**len(hand) + get_cards_value(hand,translate)
if __name__ == "__main__":
    with open("input") as f:
        lines = f.readlines()
        hands = [ Hand(line.split()[0],line.split()[1]) for line in lines]
        sorted_hands = sorted(hands, key=lambda hand: hand.value)
        print(sum([sorted_hands[i].bet *(int(i)+1) for i in range(len(sorted_hands))]))
        hands = [ Hand(line.split()[0],line.split()[1],tranlate_joker,True) for line in lines]
        sorted_hands = sorted(hands, key=lambda hand: hand.value)
        print(sum([sorted_hands[i].bet *(int(i)+1) for i in range(len(sorted_hands))]))