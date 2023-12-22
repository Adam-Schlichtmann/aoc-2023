import re
import os

file = open('./DAY_02/INPUT_02.txt', 'r')
lines = list(map(lambda x: x.strip(), file.readlines()))


# class Round:
#     def __init__(self, line):


class Game:
    def __init__(self, line):
       id, rounds = self.parse(line)
       self.id = id
       self.rounds = rounds
    
    def parse(self, line):
        [start, end] = line.split(':')
        raw_rounds = end.split(';')
        rounds = []
        for r in raw_rounds:
            cubes = r.split(',')
            round_obj = {
                "red": 0,
                "blue": 0,
                "green": 0
            }
            for cube in cubes:
                cleaned_cube = cube.strip()
                [value, key] = cleaned_cube.split(' ')
                round_obj.update({key: round_obj.get(key, 0) + int(value)})
            rounds.append(round_obj)


        return int(re.sub(r'[^\d]+', '', start)), rounds
    
    def pretty_print(self):
        print("Game {}:".format(self.id))
        for r in self.rounds: 
            print("    === ROUND ===")
            for cube in r.items():
                print("    {}".format(cube))

    def get_power(self):
        min_r = 0
        min_g = 0
        min_b = 0
        for r in self.rounds:
            if r.get('red') > min_r:
                min_r = r.get('red')
            if r.get('green') > min_g:
                min_g = r.get('green')
            if r.get('blue') > min_b:
                min_b = r.get('blue')
        return min_r * min_g * min_b

            
            
total = 0
for line in lines:
    g = Game(line)
    if all(r.get("red") <= 12 for r in g.rounds) and all(r.get("green") <= 13 for r in g.rounds) and all(r.get("blue") <= 14 for r in g.rounds):
        total += g.id

print("Solution Part 1: {}".format(total))

total = 0
for line in lines:
    g = Game(line)
    total += g.get_power()

print("Solution Part 2: {}".format(total))