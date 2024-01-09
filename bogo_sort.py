import random
import datetime
import sys


def bogo_sort(arr):
    start = datetime.datetime.now()
    count = 0
    while arr != sorted(arr):
        random.shuffle(arr)
        sys.stdout.write(f"\rChecking: {arr}")
        sys.stdout.flush()
        count += 1

    sys.stdout.write("\n")
    sys.stdout.flush()
    return datetime.datetime.now() - start, count


my_list = [5, 3, 9, 1, 4, 8, 6]
print("Unserted list:", my_list)
time, counts = bogo_sort(my_list)
print("Sorted list:", my_list)
print(f"Time: {time};Counts: {counts}")
