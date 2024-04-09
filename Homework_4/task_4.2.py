def reverse_range_iterative(L, left, right):
    while left < right:
        x = L[left]
        L[left] = L[right]
        L[right] = x
        left = left + 1
        right = right - 1
def reverse_range_recursive(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        reverse_range_recursive(L, left + 1, right - 1)

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse_range_iterative(L, 3,6)
print(L)

reverse_range_recursive(L, 3, 6)
print(L)
