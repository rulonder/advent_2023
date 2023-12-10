
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