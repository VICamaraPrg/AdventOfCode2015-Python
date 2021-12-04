"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
"""

from os import closerange


f = "inputs/day-3.txt"
path = [line.strip() for line in open(f).read()]

def part1(x=0, y=0):
    route = {(0,0)}

    for p in path:
        if p == "^":
            y += 1
        elif p == "v":
            y -= 1
        elif p == ">":
            x += 1
        elif p == "<":
            x -= 1
        route.add((x,y))
    
    return len(route)



def part2(c=0, x=0, y=0, X=0, Y=0):
    route = {(0,0)}

    for p in path:
        if c % 2 == 0:
            if p == "^":
                y += 1
            elif p == "v":
                y -= 1
            elif p == ">":
                x += 1
            elif p == "<":
                x -= 1
            route.add((x,y))
        else:
            if p == "^":
                Y += 1
            elif p == "v":
                Y -= 1
            elif p == ">":
                X += 1
            elif p == "<":
                X -= 1
            route.add((X,Y))

        c += 1

    return len(route)

print("Part 1:", part1())
print("Part 2:", part2())
