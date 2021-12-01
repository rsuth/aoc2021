with open('./input') as f:
    numbers = []
    raw_lines = f.readlines()
    for l in raw_lines:
        numbers.append(int(l.strip()))
    

def part1(nums):
    count = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            count += 1
    return count

print(part1(numbers))

def part2(nums):
    count = 0
    for i in range(3, len(nums)):
        if sum(nums[i-2:i+1]) > sum(nums[i-3:i]):
            count += 1
    return count

print(part2(numbers))