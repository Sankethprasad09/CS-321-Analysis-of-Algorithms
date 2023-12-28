def max_independent_set(nums):
    n = len(nums)

    if n == 0 or max(nums) < 0:
        return []

    if n == 1:
        return [nums[0]] if nums[0] > 0 else []

    dp = [0] * n
    dp[0] = max(0, nums[0])
    dp[1] = max(dp[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    res = []
    i = n - 1
    while i >= 0:
        if dp[i] == dp[i - 1]:
            i -= 1
        else:
            res.append(nums[i])
            i -= 2

    return res[::-1]


if __name__ == "__main__":
    input_nums = input("Enter a list of numbers separated by spaces: ")
    nums = list(map(int, input_nums.split()))
    result = max_independent_set(nums)
    print("The maximum independent set is:", result)
