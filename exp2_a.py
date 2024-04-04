def merge(arr, low, mid, high):
    lsize = mid - low + 1
    rsize = high - mid

    larr = [0] * lsize
    rarr = [0] * rsize

    # create leftarray and rightarray
    for i in range(0, lsize):
        larr[i] = arr[low + i]

    for j in range(0, rsize):
        rarr[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = low

    while i < lsize and j < rsize:
        if larr[i] < rarr[j]:
            arr[k] = larr[i]
            i += 1
        else:
            arr[k] = rarr[j]
            j += 1
        k += 1

    while i < lsize:
        arr[k] = larr[i]
        i += 1
        k += 1

    while j < rsize:
        arr[k] = rarr[j]
        j += 1
        k += 1


def mergesort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort(arr, low, mid)
        mergesort(arr, mid + 1, high)
        merge(arr, low, mid, high)


arr = [12, 11, 13, 5, 6]
mergesort(arr, 0, len(arr) - 1)
print("sorted array after mergesort  is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=' ') 