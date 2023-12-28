# PowerSet.py
def powerset(inputSet):
    result = []
    current_set = []

    def backtrack(start):
        result.append(list(current_set))
        for i in range(start, len(inputSet)):
            current_set.append(inputSet[i])
            backtrack(i + 1)
            current_set.pop()

    backtrack(0)
    return result

# Taking user input
input_list = input("Enter the numbers separated by spaces: ").split()
input_set = [int(num) for num in input_list]

# Calculating and printing the powerset
result = powerset(input_set)
print(result)

