
from collections import defaultdict
from functools import reduce
from math import gcd
from pathlib import Path
from typing import Mapping


def get_key_values(line:str):
    key, values = line.split("=")
    values = values.replace("(","").replace(")","").split(",")
    return (key.strip(), {"L":values[0].strip(),"R":values[1].strip()})
def get_steps(line:str):
    return [step for step in line.strip()]
def distance_zzz(values,steps:[str]):
        key = "AAA"
        step_index = 0
        while key != "ZZZ":
            next = step_index % len(steps)
            next_step = steps[next]
            key = values[key][next_step]
            step_index+=1
        return step_index
def finished_z(keys:[str]):
     return all([key.endswith('Z') for key in keys])
def get_period(key:str,values:Mapping[str,Mapping[str,str]],steps:[str]):
    step_index = 0
    while step_index < 1000*len(steps) :
        if key.endswith("Z"):
            print("z position", step_index) 
            return step_index
            # print(step_index)
        next = step_index % len(steps)
        next_step = steps[next]
        key = values[key][next_step]
        step_index+=1
    return step_index
     
def mcm(a:int,b:int):
    return int((a*b)/gcd(a,b))
def merge_periods(period1:int, positions1:[int], period2:int, positions2:[int],bias:int):
    # adjust for bias
    positions1b = [position-bias for position in positions1]
    positions2b = [position-bias for position in positions2]
    mcm_12 = mcm(period1,period2)
    n1 = 0
    n2 = 0
    index2 = 0
    index1 = 0
    matches = []
    position2 = positions2b[index2]
    position1 = positions1b[index1]
    while position1 < mcm_12:
        if index1 >= len(positions1b):
            # advance one period
            index1 = 0
            n1+=1
        position1 = positions1b[index1] + period1*n1
        # check if position1 is in positions2b
        while position2 <= position1:
            if position2 == position1:
                matches.append(position1)
                index1+=1
                break
            else:
                index2 +=1
                if index2 >= len(positions2b):
                    # advance one period
                    index2 = 0
                    n2+=1
                position2 = positions2b[index2] + period2*n2
        index1+=1
    return mcm_12 ,[match + bias for match in matches]
            

if __name__ == "__main__":
    with open("input") as f:
        lines = f.readlines()
        steps = get_steps(lines[0])
        values = dict([get_key_values(line) for line in lines[2:]])
        # first part
        print(distance_zzz(values,steps))
        # second part
        keys = [key for key in values.keys() if key.endswith("A")]
        results=[ get_period(ky,values,steps) for ky in keys]
        periods = [result for result in results]
        mcm_periods = reduce(mcm,periods)
        print(mcm_periods)