def binarySearch(arr, target):
    if len(arr) == 0: return -1
    first, last = 0, len(arr)
    mid = (first + last) // 2
    midthing = arr[mid]
    if midthing == target: return mid
    if midthing > target: return binarySearch(arr[:mid],target)
    result = binarySearch(arr[mid+1:],target)
    return -1 if result == -1 else mid + 1 + result

def binarySearchWithDuplicates(arr, target):
    randomone = binarySearch(arr,target)
    if randomone > 0:
        lastone = randomone
        firstone = randomone
        randomone = binarySearch(arr[:randomone], target)
        while randomone > -1:
            firstone = randomone
            randomone = binarySearch(arr[:randomone], target)
        randomone = binarySearch(arr[lastone+1:], target)
        while randomone > -1:
            lastone += randomone + 1
            randomone = binarySearch(arr[lastone+1:], target)
        return firstone, lastone
    return (-1, -1)
    
for i in range(0, 10):
    print(binarySearch([1,2,3,4,5,6], i))

for i in range(0, 10):
    print(binarySearchWithDuplicates([1,1,1,1,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6], i))
