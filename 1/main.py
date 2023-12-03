import re
def get_number(line):
    x = re.findall("[0-9]", line)
    first_digit = x[0].strip()
    last_digit = x[-1].strip()
    return int(first_digit)*10+int(last_digit)

translate = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
    }

numbers_regexp = re.compile(r"one|two|three|four|five|six|seven|eight|nine")

def clean_line(line):
    matches = numbers_regexp.findall( line)
    if len(matches):
        match = matches[0]
        line = line.replace(match, str(translate[match]),1)
        match = matches[-1]
        line = line.replace(match, str(translate[match]))
    return line

def translate_number(string):
    for tanslation in translate:
        string = string.replace(tanslation, str(translate[tanslation]))
    return string

def get_number2(line):
    # line = clean_line(line)
    x= re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))',line)
    # x = re.findall("one|two|three|four|five|six|seven|eight|nine|[0-9]", line)
    if len(x) == 0:
        return line
    first_digit = translate_number(x[0].strip())
    last_digit = translate_number(x[-1].strip())
    return int(first_digit)*10+int(last_digit)

# test should be 303
if __name__ == "__main__":
    sum = 0
    with open("input") as f:
        lines = f.readlines()
        print(len(lines))
        for line in lines:
            sum += get_number2(line)
    print(sum)


