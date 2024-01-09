def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


my_list = [1, 2, 3, 9, 1, 4, 8, 6]
print("Unsorted list:", my_list)
sorted_list = quick_sort(my_list)
print("Sorted list:", sorted_list)
