

def get_number(line):
    kv=line.split()
    return int(kv[0])

class SetOfCubes:
    red = 0
    green = 0
    blue = 0
    def __init__(self, set_of_cubes):
        #   1 red, 2 green, 6 blue
        sets = set_of_cubes.split(",")
        for set in sets:
            set = set.strip()
            if "red" in set:
                self.red = get_number(set)
            elif "green" in set:
                self.green = get_number(set)
            elif "blue" in set:
                self.blue = get_number(set)
    def __gt__(self, other):
        return self.red > other.red or self.green > other.green or self.blue > other.blue
    def max(self, other):
        max_red = max(self.red, other.red)
        max_green = max(self.green, other.green)
        max_blue = max(self.blue, other.blue)
        return SetOfCubes('{} red, {} green, {} blue'.format(max_red, max_green, max_blue))
    def power(self):
        return self.red * self.green * self.blue

reference_set = SetOfCubes("12 red, 13 green, 14 blue")

class Game:
    id = 0
    sets=[]
    def __init__(self, game):
        self.sets = []
        def_values = game.split(":")
        self.id = int(def_values[0].split()[1])
        sets = def_values[1].split(";")
        for set in sets:
            self.sets.append(SetOfCubes(set))
    def is_feasible(self):
        valid = True
        for set in self.sets:
            if set > reference_set:
                return False
        return valid
    def get_min_set(self):
        min_set = self.sets[0]
        for set in self.sets:
            min_set=min_set.max(set)
        return min_set

if __name__ == "__main__":
    sum = 0
    sum_power = 0
    test = Game('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green')
    print(test.is_feasible())
    with open("input") as f:
        lines = f.readlines()
        for line in lines:
            game = Game(line)
            sum_power += game.get_min_set().power()
            if game.is_feasible():
                 sum += game.id
    print("first Game ::",sum)
    print("2nd Game ::",sum_power)