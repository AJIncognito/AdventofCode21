#AOC2021 Day 3b

## Baseline variables
example_input = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

zero_counter = []
one_counter = []
gamma_counter = []
epsilon_counter = []
oxygen_rating = []
co2_rating = []

## populate counters
def fill_counters(size):
    for i in range(size):
        zero_counter.append(0)
        one_counter.append(0)
        gamma_counter.append(0)
        epsilon_counter.append(0)

def clear_counters():
    zero_counter = []
    one_counter = []
    gamma_counter = []
    epsilon_counter = []

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

##with open('input.txt') as file:
##    lines = file.readlines()
##    lines = [line.rstrip() for line in lines]

field_size = len(example_input)
fill_counters(field_size)

for i in example_input:
    count_input(i)


for i in range(len(zero_counter)):
    if zero_counter[i] < one_counter[i]:
        gamma_counter[i] = 1

print("Gamma counter is: ", gamma_counter)
print("Example input is: ", example_input)
a, b = 0, 1
print("test pattern is: " + str(gamma_counter[0]) + ".")

#for inputs in example_input:
#    test_string = inputs
#
#    print("test string: ", test_string)
#    print("AB output: ", test_string[0: 1])
#
#    if int(test_string[0: 1]) == gamma_counter[0]:
#        print("Matched.")
#        oxygen_rating.append(test_string)

oxygen_output = example_input
print("initial oxygen output: ", oxygen_output)
for i in range(len(oxygen_output)):
    if oxygen_output[i]:
        if str(oxygen_output[i])[0:1] == str(gamma_counter[0]):
            oxygen_output.pop(i)
        if

print("oxygen output: ", oxygen_output)
#oxygen_rating = [ele for ele in example_input if ele[a: b]] == str(gamma_counter[0])

#print("Updated oxygen rating: ", oxygen_rating)
