import re

def part1():
    with open("input2.txt", "r") as file: # Read input file
        content = file.read()
        separated_content = content.split(",")

    total = 0 # Total to return
    for ranges in separated_content:
        id1, id2 = ranges.split('-') # Find the 2 nums

        for num in range(int(id1), int(id2) + 1): # Check entire range (slow)
            if bool(re.search(r'^(.+)\1$', str(num))) and len(str(num))%2 == 0: # Look for double repeats only via regex, for this part the length MUST be even
                total += num

    return total

def part2():
    with open("input2.txt", "r") as file:
        content = file.read()
        separated_content = content.split(",")
        
    total = 0
    for ranges in separated_content:
        id1, id2 = ranges.split('-')

        for num in range(int(id1), int(id2) + 1):
            if bool(re.search(r'^(.+)\1+$', str(num))): # Change 1 -> 1+ in regex for triple/inf repeats, remove even len check (odd len allowed)
                total += num

    return total

if __name__ == "__main__":
    print(part1())
    print(part2())
