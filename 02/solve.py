dirs = {
    "f": (1,0),
    "u": (0,-1),
    "d": (0,1)
}

# horizontal, aim, depth
pos = (0,0,0)

with open('./input.txt') as fh:
    for instruction in fh:
        d = instruction[0]
        s = int(instruction.split()[1])
        pos = (
            pos[0] + s*dirs[d][0],
            pos[1] + s*dirs[d][1],
            pos[2] + s*dirs[d][0]*pos[1])

print(f"part1: {pos[0]*pos[1]}")
print(f"part2: {pos[0]*pos[2]}")