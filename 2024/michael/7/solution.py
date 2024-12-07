import sys

def parseLine(line):
    (val, nums) = line.split(': ')
    nums = [int(num) for num in nums.split(' ')]
    return (int(val), nums)


## P1
def isFeasible(val, nums):
    if len(nums) == 1:
        return val == nums[0]
    
    return isFeasible(val - nums[-1], nums[:-1]) or isFeasible(val / nums[-1], nums[:-1])

## P2
def isFeasibleP2(val, accum, nums):
    if len(nums) == 0:
        return val == accum
    
    return (
            isFeasibleP2(val, accum + nums[0], nums[1:]) 
            or isFeasibleP2(val, accum * nums[0], nums[1:])
            or isFeasibleP2(val, int(str(accum) + str(nums[0])), nums[1:])
            )


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = [parseLine(line) for line in f.readlines()]

    p1_total = 0
    p2_total = 0
    for (val, nums) in lines:
        if isFeasible(val, nums):
            p1_total += val
        if isFeasibleP2(val, nums[0], nums[1:]):
            p2_total += val
    print(p1_total)
    print(p2_total)