def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = list(filter(lambda x: x < pivot, arr))
    center = [i for i in arr if i == pivot]
    right = list(filter(lambda x: x > pivot, arr))
    return quick_sort(left) + center + quick_sort(right)


def find_largest_k_el(arr):
    sorted_array = quick_sort(arr)
    largest_k_el = sorted_array[-k]
    return largest_k_el


def index_k_largest_el(arr, k):
    index = arr.index(k)
    return index


arr = [15, 7, 22, 9, 36, 2, 42, 18]
k = 3
result = find_largest_k_el(arr)
index = index_k_largest_el(arr, result)
print(f'Елемент: {result} з індексом: {index}')
