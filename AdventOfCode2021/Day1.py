import time



def part_1(input: str) -> str:
    ints = [int(s) for s in input.splitlines()]

    last = ints[0]
    count = 0
    for i in ints[1:]:
        if i > last:
            count += 1

        last = i

    return str(count)


def part_2(input: str) -> str:
    ints = [int(s) for s in input.splitlines()]
    windows = list(clump(ints, 3))

    s = sum(windows[0])
    c = 0
    for w in windows[1:]:
        w_sum = sum(w)
        if w_sum > s:
            c += 1

        s = w_sum

    return str(c)


example = """199
200
208
210
200
207
240
269
260
263"""

if __name__ == '__main__':
    t = time.time()
    res = part_1(open("Day1.txt").read())
    end = time.time()
    print(f'Part 1: {res}, {end-t}')

    
### FOR PART 2

def solve_part_2(nums):
    res = 0
    prev = float('inf')
    curr = nums[0] + nums[1]
 
    for i in range(2, len(nums)):
        curr += nums[i]
 
        if curr > prev:
            res += 1
 
        prev = curr
        curr -= nums[i - 2]
 
    return res
 
if __name__ == '__main__':
    with open('Day1.txt') as f:
        nums = [int(line) for line in f.readlines()]
        
print(solve_part_2(nums))
