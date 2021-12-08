#initialize list
test_list = ['101', '001', '100', '111', '010']

print("Original list: " + str(test_list))

# substring
subs = '1'

# range
i, j = 0, 1

res = [ele for ele in test_list if ele[i: j] == subs]

print("Result: " + str(res))
