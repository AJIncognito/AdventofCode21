#AOC2021 Day 3a

## Baseline variables
example_input = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

zero_counter = []
one_counter = []
gamma_counter = []
epsilon_counter = []


## populate counters
def fill_counters(size):
    for i in range(size):
        zero_counter.append(0)
        one_counter.append(0)
        gamma_counter.append(0)
        epsilon_counter.append(0)

## increment counters based on a single n-digit input
def count_input(input):
    elements = list(input)
    for i in range(len(elements)):
        if elements[i] == '0':
            zero_counter[i] += 1
        else:
            one_counter[i] += 1

## convert counter list to a binary number
def convert_counter(input):
    output_str = "0b"
    for x in input:
        output_str += str(x)
    ## print("Output string is: ", output_str)
    ## print("Base 10 output: ", int(output_str, 2))
    return int(output_str, 2)

def gamma_to_epsilon(gamma):
    output = []
    for x in range(len(gamma)):
        if(gamma[x]) == 0:
            output.append(1)
        else:
            output.append(0)
    return output

## start of program actions

with open('input.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

field_size = len(lines[0])
fill_counters(field_size)

for i in lines:
    count_input(i)


for i in range(len(zero_counter)):
    if zero_counter[i] < one_counter[i]:
        gamma_counter[i] = 1

gamma_final = convert_counter(gamma_counter)
epsilon_final = convert_counter(gamma_to_epsilon(gamma_counter))


print("Final answer is: ", gamma_final * epsilon_final) 