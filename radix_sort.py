def radix_sort_lsd(arr):
    max_num = max(arr)
    exp = 1
    n = len(arr)

    while max_num // exp > 0:
        counting_sort(arr, n, exp)
        exp *= 10

def counting_sort(arr, n, exp):
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

my_list = [170, 45, 75, 90, 802, 24, 2, 66]
print("Unsorted list:", my_list)
radix_sort_lsd(my_list)
print("Sorted list:", my_list)
