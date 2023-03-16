# Q1-1
def find_max(numbers):
    max_val = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_val:
            max_val = numbers[i]    
    return max_val

# Q1-2
def find_position(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1
  
# Q2-1
def count(input):
  counts = {}
    for char in input:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts
  
# Q2-2
def group_by_key(input):
    sums = {}
    for d in input:
        for key, value in d.items():
            if key in sums:
                sums[key] += value
            else:
                sums[key] = value
    return sums
