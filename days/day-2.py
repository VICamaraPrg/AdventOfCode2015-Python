"""
--- Day 2: I Was Told There Would Be No Math ---
"""
import re 
# l,w,h

f = "inputs/day-2.txt"
dimensions = [line.strip() for line in open(f).readlines()]

def part1(paper=0):
    for d in dimensions:
        data = re.findall(r"(\d+)", d)
        l, w, h =  int(data[0]), int(data[1]), int(data[2])

        needed = (2*l*w) + (2*w*h) + (2*h*l)
        slack = min((l*w), (w*h), (h*l))
        paper += needed + slack
    
    return paper

"""
--- Part Two ---
"""


def part2(wrap=0, bow=0, paper=0):
    for d in dimensions:
        data = re.findall(r"(\d+)", d)
        l, w, h =  int(data[0]), int(data[1]), int(data[2])

        wrap = 2 * min(l+w, w+h, h+l)
        bow = (l*w*h)
        paper += wrap + bow
    
    return paper


print("Part 1:", part1())
print("Part 2:", part2())
