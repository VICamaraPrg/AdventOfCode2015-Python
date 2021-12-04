"""
--- Day 1: Not Quite Lisp ---
"""

from collections import Counter

f = "inputs/day-1.txt"
instructions = [c.strip() for c in open(f).read()]

def part1():
    d = Counter(instructions)
    return (d.get("(") - d.get(")"))

"""
--- Part Two ---
"""

def part2(floor=0):
    for i in range(len(instructions)):
        if floor < 0:
            return i
        else:
            if instructions[i] == "(":
                floor += 1
            else:
                floor -= 1

print("Part 1:",part1())
print("Part 2:",part2())