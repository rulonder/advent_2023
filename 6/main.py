import functools
def distance(race_time:int, start_time:int)->int:
    return start_time * (race_time-start_time)
def race_options(race_time:int,distance_record:int)->int:
    return sum([ 1 for time in range(race_time) if distance(race_time,time) > distance_record ])
if __name__ == "__main__":
    with open("input") as f:
        lines = f.readlines()
        times = [int(x) for x in lines[0].split()[1:]]
        distances = [int(x) for x in lines[1].split()[1:]]
        print(functools.reduce(lambda x,y: x*y ,[ race_options(times[race_i],distances[race_i]) for race_i in range(len(times))],1))
        time2 = int(''.join(lines[0].split()[1:]))
        distnce2 = int(''.join(lines[1].split()[1:]))
        print( time2,distnce2,race_options(time2,distnce2) )

