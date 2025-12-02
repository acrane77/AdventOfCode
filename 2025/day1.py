def part1():
    with open("input1.txt", "r") as file: # Read input
        content = file.read()
        separated_content = content.split('\n')
    
    dial = 50 # Starting position of dial
    password = 0 # Password is number of times dial == 0

    for rotation in separated_content:
        direction = rotation[0] # Direction always first letter
        magnitude = int(rotation[1:]) % 100 # Magnitude is rest of entry, modulo 100 to normalize

        if direction == 'L': # Left direction, subtract and if negative turn it positive
            dial -= magnitude
            if dial < 0:
                dial = 100 + dial

        elif direction == 'R': # Right direction, add and if > 100 normalize to < 100 via modulus
            dial += magnitude
            if dial >= 100:
                dial = dial%100
                
        if dial == 0: # Increment password if dial == 0
            password += 1

    return password

def part2():
    with open("input1.txt", "r") as file: # Read input
        content = file.read()
        separated_content = content.split('\n')
    
    dial = 50 # Starting position of dial
    password = 0 # Password is number of times dial == 0
    prev_dial = dial

    for rotation in separated_content:
        direction = rotation[0] # Direction always first letter
        magnitude = int(rotation[1:]) # Can't apply modulus too early now as its a "click"
        
        if magnitude >= 100:
            password += magnitude//100 # Calculate number of "clicks"
            magnitude = magnitude%100 # Re-apply modulus

        if direction == 'L': # Left direction, subtract and if negative turn it positive
            dial -= magnitude

            if dial < 0:
                dial += 100
                if prev_dial != 0:
                    password += 1 # "Click"
            elif dial == 0:
                password += 1

        elif direction == 'R': # Right direction, add and if > 100 normalize to < 100 via modulus
            dial += magnitude

            if dial >= 100:
                dial = dial%100
                if prev_dial != 0:
                    password += 1 # "Click"

        prev_dial = dial
    return password
    

if __name__ == "__main__":

    print(part1())
    print(part2())
