# The idea of this one is that you are given a number of integers, 0 or 1, and you are adding them up.
# The algorithmic twist is that you can take a contiguous region of numbers, and flip them between 0 and 1.
# So, find the largest sum you could make where some contiguous region is being flipped.

def sumwithinv(nums, L, R):
    return sum(nums[:L]) + sum(0 if i == 1 else 1 for i in nums[L:R+1]) + sum(nums[R+1:])

N = int(input())
nums = [int(i) for i in raw_input().split(' ')]

class Region:
    def __init__(self,L,R):
        self.sum = sumwithinv(nums,L,R)
        self.L = L
        self.R = R
    def __str__(self):
        return 'L: ' + str(self.L) + ' R: ' + str(self.R)

regions = []

started = False
for i in range(len(nums)):
    if nums[i] == 0 and not started:
        L = i
        started = True
    elif nums[i] == 1 and started:
        regions.append(Region(L,i-1))
        started = False
    i = i + 1

if len(regions) == 0:
    print(sum(nums))
    sys.exit(0)

maxregion = Region(regions[0].L,regions[len(regions)-1].R)
trimming = True
while trimming and len(regions) > 1:
    trimming = False
    removeleft = regions[1:]
    smallerregion = Region(removeleft[0].L,removeleft[len(removeleft)-1].R)
    if smallerregion.sum >= maxregion.sum:
        regions = removeleft
        maxregion = smallerregion
        trimming = True
trimming = True
while trimming and len(regions) > 1:
    trimming = False
    removeright = regions[:-1]
    smallerregion = Region(removeright[0].L,removeright[len(removeright)-1].R)
    if smallerregion.sum >= maxregion.sum:
        regions = removeright
        maxregion = smallerregion
        trimming = True
    
print(maxregion.sum)
