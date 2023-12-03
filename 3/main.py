
from collections import defaultdict 
class Number:
    value: int = None
    start: int = None
    end: int = None
    def __init__(self, line, start):
        # find start
        for position in range(start, len(line)):
            char = line[position]
            if char in "123456789":
                self.start = position
                self.end = position
                break
        # if no start found, return
        if self.start == None:
            return
        # find end
        for position in range(self.start+1, len(line)):
            char = line[position]
            if char not in "0123456789":
                break
            self.end = position
        # set value
        if self.start != None:
            self.value = int(line[self.start:self.end+1])

class Map:
    def __init__(self, lines):
        self.map = [line.rstrip() for line in lines]
        self.rows = len(lines)
        self.columns = len(lines[0].rstrip())
        self.sum = 0
        self.numbers = []
        self.gears= defaultdict(list)
    def get_around(self, start,end, row_number):
        positions = []
        if start != None:
            # add upper and lower position
            for i in range(start-1, end+2):
                positions.append((row_number-1, i))
                positions.append((row_number+1, i))
            # add left position
            positions.append((row_number, start-1))
            # add right position
            positions.append((row_number, end+1))
        return positions
    def check_number(self,number,row_number):
        around = self.get_around(number.start, number.end, row_number)
        locations = 0
        for position in around:
            if self.is_Symbol(position[0], position[1]):
                locations += 1
            # check for gears
            if self.is_gear(position[0], position[1]):
                self.gears[position].append(number)
        return locations
    def is_Symbol(self, row, column):
        # outside map are not considered
        if row < 0 or row >= self.rows or column < 0 or column >= self.columns:
            return False
        return self.map[row][column] not in "0123456789."
    def is_gear(self, row, column):
        # outside map are not considered
        if row < 0 or row >= self.rows or column < 0 or column >= self.columns:
            return False
        return self.map[row][column] == "*"
    def check_row(self, row_number):
        start = -1
        while start != None and start < self.columns:
            number = Number(self.map[row_number], start+1)
            symbols = self.check_number(number, row_number)
            if number.value and symbols>0:
                self.numbers.append(number)
                self.sum += number.value 
            start = number.end
    def check_matrix(self):
        for row_number in range(self.rows):
            self.check_row(row_number)
    def get_sum(self):
        self.check_matrix()
        return self.sum
    def get_gear_sum(self):
        sum = 0
        for key,values in self.gears.items():
            if len(values) == 2:
                sum += values[0].value * values[1].value
        return sum


if __name__ == "__main__":
    with open("test") as f:
        lines = f.readlines()
        map = Map(lines)
        print(map.get_sum())
        print(map.get_gear_sum())
    with open("input") as f:
        lines = f.readlines()
        map = Map(lines)
        print(map.get_sum())
        print(map.get_gear_sum())