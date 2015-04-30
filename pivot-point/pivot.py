# Idea: Find a pivot point so that the sum of the items in the array below the pivot
#       is the sum of the items above the pivot.
#       Excluding the pivot itself.
# Input: An array of integers.
# Output: A pivot point, or -1 if none found.
#         And it takes worst case O(N) time and space.
def pivot(A):
    N = len(A)
    cumulativesums = [0]*N # sums of integers before i
    revcumulativesums = [0]*N # sums of integers after i
    cumsum = 0
    revsum = 0
    for i in range(1,N):
        cumsum += A[i-1]
        revsum += A[N-i]
        cumulativesums[i] = cumsum
        revcumulativesums[N-i-1] = revsum
    for i in range(N):
        if cumulativesums[i] == revcumulativesums[i]:
            return i
    return -1
