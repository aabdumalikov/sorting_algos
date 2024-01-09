def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


my_list = [5, 3, 9, 1, 4, 8, 6]
print("Unsorted list:", my_list)
bubble_sort(my_list)
print("Sorted list:", my_list)
