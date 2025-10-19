# amira mohamed zakaria refat --section 5

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

numbers = [29, 10, 14, 1000, 45, 35]
selection_sort(numbers)
print("Sorted list:", numbers)