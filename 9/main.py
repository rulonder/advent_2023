def next_history(history:[int]):
    if history[-1] == 0:
        return 0
    else:
        next_one = next_history([ history[i+1]-history[i] for i in range(len(history)-1)])
        return history[-1] + next_one

def back_history(history:[int]):
    if all(x==0 for x in history):
        return 0
    else:
        next_one = back_history([ history[i+1]-history[i] for i in range(len(history)-1)])
        return history[0] - next_one

if __name__ == "__main__":
    with open("input") as f:
        lines = f.readlines()
        sum = 0
        sum2 = 0
        for line in lines:
            history = [int(x) for x in line.split(" ")]
            sum += next_history(history)
            sum2 += back_history(history)
        print(sum, sum2)