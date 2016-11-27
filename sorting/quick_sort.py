def quick_sort(arr, first, last):
    """ Quicksort
        Complexity: best O(n) avg O(n log(n)), worst O(N^2)
    """
    if first < last:
        pos = partition(arr, first, last)
        # Start our two recursive calls
        quick_sort(arr, first, pos-1)
        quick_sort(arr, pos+1, last)

def partition(arr, first, last):
    wall = first
    for pos in xrange(first, last):
        if arr[pos] < arr[last]: # last is the pivot
            arr[pos], arr[wall] = arr[wall], arr[pos]
            wall += 1
    arr[wall], arr[last] = arr[last], arr[wall]
    return wall

array = [1,5, 7,4,3,2,1,9,0,10,43,64]
print(array)
print(quick_sort(array, 0, len(array)-1))
print(array)
