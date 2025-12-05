def part1():
    with open("input5.txt", "r") as file:
        content = file.read()
        separated_content = content.split("\n")
    
    split_index = separated_content.index('')
    str_pairs = separated_content[:split_index]
    nums = separated_content[split_index + 1:]
    
    pairs = []
    for pair in str_pairs: # parse 'n-n' to (n, n)
        r1, r2 = pair.split('-')
        pairs.append((int(r1), int(r2)))

    total = 0
    s = set()
    for pair in pairs: # if num in between a pair, its "fresh". Add to set to ensure no duplicates 
        for num in nums:
            if int(num) >= pair[0] and int(num) <= pair[1]:
                if num not in s:
                    total += 1
                    s.add(num)
                
    return total

def part2():
    with open("input5.txt", "r") as file:
        content = file.read()
        separated_content = content.split('\n')
    split_index = separated_content.index('')
    str_pairs = separated_content[:split_index] # only care about pairs for pt2

    pairs = []
    for pair in str_pairs: # parse again
        r1, r2 = pair.split('-')
        r1, r2 = int(r1), int(r2)
        pairs.append((r1, r2))
    
    pairs.sort() 
    total = 0
    current_start = pairs[0][0]
    current_end = pairs[0][1]
    
    for start, end in pairs[1:]:
        if start > current_end: # Not overlapping, start > last end
            total += current_end - current_start + 1
            current_start = start
            current_end = end

        elif start <= current_end: # Overlapping, start < last end
            current_end = max(current_end, end) # extend range with max()

    total += current_end - current_start + 1 # Add final range to total
    return total
        
if __name__ == "__main__":
    print(part1())
    print(part2())