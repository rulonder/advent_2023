from io import TextIOWrapper
import operator

def parse_seeds(line)->[int]:
    return [int(s) for s in line.split()[1:]]

def parse_seeds_pairs(line)->['RangeIter']:
    return RangeIter.from_line(line)

class RangeIter:
  def __init__(self,start:int, end:int): 
      self.start = start
      self.end = end
  @classmethod    
  def from_line(cls,line)->['RangeIter']:
    values = line.split()[1:]
    ranges = []
    for i in range(0, len(values), 2):
        start = int(values[i])
        end = start + int(values[i+1])
        ranges.append(RangeIter(start, end))   
    return ranges
  def intersection(self, other:'RangeIter') -> (['RangeIter'], ['RangeIter']):
      if other.end < self.start or other.start >= self.end:
          return [],[other] 
      # find intersection for start
      new_start = max(self.start, other.start)
      new_end = min(self.end, other.end)
      intersections = [] 
      intersections.append(RangeIter(new_start, new_end))
      # find remaining
      remaining = []
      if other.start < new_start:
          remaining.append(RangeIter(other.start, new_start))   
      if other.end > new_end:
          remaining.append(RangeIter(new_end,other.end))   
      return intersections, remaining
  def get(self,index:int)->int:
      return self.start + index
  def get_index(self,value:int)->int:
      return value - self.start
  def __eq__(self, other):
     return self.start == other.start and self.end == other.end
  def __repr__(self) -> str:
      return "{}-{}".format(self.start, self.end)

def parse_header(line)->[str,str]:
    if "map:" in line:
        return operator.itemgetter(0,2)(line.strip().split()[0].split('-'))
    return None
def parse_value(line:str)->[int, int, int]:
    if line.strip() == '':
        return None
    dest_start, src_start ,values_range = line.strip().split()
    return int(dest_start), int(src_start) ,int(values_range)

class Range_Mapper(object):
    def __init__(self, dest_start:int, src_start:int ,values_range:int):
        self.dest = RangeIter(dest_start,dest_start+values_range)
        self.src = RangeIter(src_start,src_start+values_range)
    def overlap(self, other:RangeIter):
        return self.src.intersection(other)
    def get_dst(self, src:RangeIter)->RangeIter:
        dest_start =  self.dest.get(self.src.get_index(src.start))
        dest_end = self.dest.get(self.src.get_index(src.end))
        return RangeIter(dest_start, dest_end)
class Mapper(object):
    src:str
    dst:str
    mappers:[Range_Mapper]
    def __init__(self):
        self.mappers = []
    def set_src_dst(self, src:str, dst:str):
        self.src = src
        self.dst = dst
    def add_mapping(self,mapper:Range_Mapper):
        self.mappers.append(mapper)
    def get_dst(self, src:[Range_Mapper])->[Range_Mapper]:
        remaining = src
        dst : [Range_Mapper]= []
        for mapper in self.mappers:
            new_remaining = []
            for remaining_mapper in remaining:
                intersections, remaining = mapper.overlap(remaining_mapper)
                dst.extend([mapper.get_dst(intersection) for intersection in intersections])
                new_remaining.extend(remaining)
            remaining = new_remaining
        dst.extend(remaining)
        return dst
class Mapping(object):
    maps : dict[str, Mapper]
    def __init__(self):
        self.maps = {}
    def add_map(self, map:Mapper):
        self.maps[map.src] = map
    def get_dest(self, src:str, dst:str, src_pos:[Range_Mapper])->[Range_Mapper]:
        next_dst = self.maps[src].dst
        next_positions = self.maps[src].get_dst(src_pos)
        if next_dst != dst:
            return self.get_dest(next_dst, dst, next_positions)
        return next_positions

def load_data(file:TextIOWrapper)->Mapping:
    mapping = Mapping()
    firstline = file.readline()
    seeds = parse_seeds(firstline)
    extra_seeds = parse_seeds_pairs(firstline)
    while True:
        line = file.readline()
        if not line:
            break
        header = parse_header(line)
        if header != None:
            map = Mapper()
            map.set_src_dst(header[0], header[1])
            while True:
                line = file.readline()
                values = parse_value(line)
                if values != None:
                    map.add_mapping(Range_Mapper(*values))
                if not line or values == None:
                    break
            mapping.add_map(map)
    return seeds ,extra_seeds,mapping

if __name__ == "__main__":
    with open("input") as f:
        seeds,extra_seeds, mapping  = load_data(f)
        min_path = min([rng.start for rng in mapping.get_dest("seed","location",extra_seeds)])
        print(min_path)
