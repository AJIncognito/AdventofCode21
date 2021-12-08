## AOC2021 - Problem 1a



with open('input.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
        
lines = list(map(int, lines))

count = 0
for i in range(len(lines)-1):
    if lines[i+1] and lines[i] < lines[i+1]:
        count+=1
print(count)


    

