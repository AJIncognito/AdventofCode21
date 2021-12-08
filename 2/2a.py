## AOC21 2a.py

horiz = 0
depth = 0
aim = 0

example_input = ['forward 5','down 5','forward 8', 'up 3', 'down 8','forward 2']

with open('input.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

for x in range(0, len(lines)):
    direction, amt = lines[x].split()
    if direction == 'forward':
        horiz += int(amt)
        depth += (int(amt) * aim)
    elif direction == 'up':
        aim -= int(amt)
    elif direction == 'down':
        aim += int(amt)

print("End horiz: ", horiz, " end depth: ", depth)
print("solution: ", horiz * depth)