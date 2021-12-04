"""
--- Day 4: The Ideal Stocking Stuffer ---
"""

import hashlib
import re

input = "yzbqklnj"

def part1():
    for x in range(100000*100000):
        hash = hashlib.md5((input + str(x)).encode()).hexdigest()
        if re.findall(r"^(0{5})", hash):
            print(hash)
            return x

"""
--- Part Two ---
"""

def part2():
    for x in range(100000*100000):
        hash = hashlib.md5((input + str(x)).encode()).hexdigest()
        if re.findall(r"^(0{6})", hash):
            print(hash)
            return x

print("Part 1:", part1())
print("Part 2:", part2())
