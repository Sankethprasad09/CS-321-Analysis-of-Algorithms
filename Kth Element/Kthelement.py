def kthElement(Arr1, Arr2, k):
    if len(Arr1) > len(Arr2):
        return kthElement(Arr2, Arr1, k)
    if len(Arr1) == 0:
        return Arr2[k - 1]
    if k == 1:
        return min(Arr1[0], Arr2[0])

    indexA = min(k // 2, len(Arr1))
    indexB = k - indexA

    if Arr1[indexA - 1] < Arr2[indexB - 1]:
        return kthElement(Arr1[indexA:], Arr2, k - indexA)
    else:
        return kthElement(Arr1, Arr2[indexB:], k - indexB)

# Example usage
Arr1 = [1, 2, 3, 5, 6]
Arr2 = [3, 4, 5, 6, 7]
k = 5
result = kthElement(Arr1, Arr2, k)
print("The element at position", k, "is", result)
