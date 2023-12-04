def numbers_to_array(set_values):
    return [int(x) for x in set_values.strip().split()]

def parse_line(line: str):
    values = line.split(":")[1].split("|")
    winning_numbers = numbers_to_array(values[0])
    own_numbers = numbers_to_array(values[1])
    matches = [ 1 for number in own_numbers if number in winning_numbers]
    return sum(matches)

def prize(matches:int):
    return 0 if matches == 0 else 2**(matches-1)

def parse_lines(lines):
    card_stack = [1 for i in range(len(lines))]
    card_matches = [parse_line(line) for line in lines]
    update_card_stack = [range(i+1,i+card_matches[i]+1) for i in range(len(card_stack))]
    for i in range(len(card_stack)):
        for j in update_card_stack[i]:
            card_stack[j] += card_stack[i]
    # first quizz
    sums = [prize(card) for card in card_matches]
    return sum(sums) , sum(card_stack) 

if __name__ == "__main__":
    with open("test") as f:
        lines = f.readlines()
        print(parse_lines(lines))
    with open("input") as f:
        lines = f.readlines()
        print(parse_lines(lines))
