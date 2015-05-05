# Binary searches. Return index of target, or -1 if target does not exist.
# With duplicates, then return indices of target.

def binarySearch(arr, target):
    if len(arr) == 0: return -1
    mid = len(arr) // 2
    midthing = arr[mid]
    if midthing == target: return mid
    if midthing > target: return binarySearch(arr[:mid],target)
    result = binarySearch(arr[mid+1:],target)
    return -1 if result == -1 else mid + 1 + result

def binarySearchWithDuplicates(arr, target):
    randomone = binarySearch(arr, target)
    if randomone < 0 : return -1, -1
    search = lambda array: binarySearch(array, target)
    findfirst = lambda array, searchfirst, first: \
                first if searchfirst == -1 \
                else findfirst(array[:searchfirst], search(array[:searchfirst]),searchfirst)
    findlast = lambda array, searchlast, last: \
               last if searchlast == -1 \
               else findlast(array[searchlast+1:], search(array[searchlast+1:]),last + searchlast + 1)
    first = findfirst(arr[:randomone],search(arr[:randomone]),randomone)
    last = findlast(arr[randomone+1:],search(arr[randomone+1:]),randomone)
    return first, last
    
for i in range(0, 10):
    print(binarySearch([1,2,3,4,5,6], i))

for i in range(0, 10):
    print(binarySearchWithDuplicates([1,1,1,1,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6], i))
