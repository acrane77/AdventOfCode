def part1():
    with open("input3.txt", "r") as file:
        content = file.read()
        separated_content = content.split('\n')

    first = 0
    second = 0
    total = 0

    for bank in separated_content:
        first = 0
        second = 0
        for i in range(len(bank)):
            if len(bank) - 1 > i and int(bank[i]) > first: # Must be greater than current first and NOT last entry of the list.
                first = int(bank[i])
                second = 0
            elif int(bank[i]) > second: # Second must be greater than current second
                second = int(bank[i])

        local_total = str(first) + str(second) # Build total
        total += int(local_total)

    return total
    
def part2():
    with open("input3.txt", "r") as file:
        content = file.read()
        separated_content = content.split('\n')

    total = 0
    max_size = 12
    for bank in separated_content:
        if len(bank) == max_size:
            total += int(bank)
        else:
            result = ""
            i = 0
            for j in range(max_size):
                remaining = max_size - j - 1
                max_index = len(bank) - remaining - 1
                best_digit = '0'
                best_pos = i

                for k in range(i, max_index + 1):
                    if bank[k] > best_digit:
                        best_digit = bank[k]
                        best_pos = k

                result += best_digit
                i = best_pos + 1

            total += int(result)

    return total

if __name__ == "__main__":
    print(part1())
    print(part2())