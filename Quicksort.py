def QuickSort(arr):
    more = [a for a in arr[1:] if a > arr[0]]
    less = [a for a in arr[1:] if a < arr[0]]
    return [] if len(arr) < 1 else [more, QuickSort(more)][len(more) > 1] + [arr[0]] + [less, QuickSort(less)][
        len(less) > 1]

a = QuickSort([5, 7, 0, 9])
print a