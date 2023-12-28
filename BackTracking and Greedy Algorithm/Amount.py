def amount(A, S):
    def backtrack(combination, target_sum, start):
        if target_sum == 0:
            result.append(list(combination))
            return
        if target_sum < 0:
            return
        for i in range(start, len(A)):
            if i > start and A[i] == A[i - 1]:
                continue
            combination.append(A[i])
            backtrack(combination, target_sum - A[i], i + 1)
            combination.pop()

    A.sort()
    result = []
    backtrack([], S, 0)
    return result

# Asking for user input
print("Enter the amount values separated by spaces:")
A = list(map(int, input().split()))
print("Enter the target sum:")
S = int(input())

# Example usage
result = amount(A, S)
print("The unique combinations are:")
print(result)

