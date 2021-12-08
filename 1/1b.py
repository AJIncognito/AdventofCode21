## AOC2021 - Problem 1b



with open('input.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
        
lines = list(map(int, lines))

## count = 0
## for i in range(len(lines)-1):
##     if lines[i+1] and lines[i] < lines[i+1]:
##        count+=1
## print(count)

print(sum(x < y for x, y in zip(lines, lines[3:])))


    

