from math import prod

def part1():
    with open("test.txt", "r") as file:
        content = file.read()
        separated_content = content.split('\n')
    
    for i in range(len(separated_content)):
        separated_content[i] = separated_content[i].split(' ')
    
    nums_list = [[num for num in row if num != ''] for row in separated_content]
    
    result_list = []
    length = len(nums_list)
    for i in range(len(nums_list[0])):
        temp_list = []
        j = 0
        while j < length:
            if nums_list[j][i] == '*' or nums_list[j][i] == '+':
                temp_list.append(nums_list[j][i])
            else:
                temp_list.append(int(nums_list[j][i]))

            j += 1
        
        result_list.append(temp_list)

    total = 0

    for i in range(len(result_list)):
        if result_list[i][-1] == '*':
            result = prod(result_list[i][:len(result_list[i])-1])
            total += result
        elif result_list[i][-1] == '+':
            result = sum(result_list[i][:len(result_list[i])-1])
            total += result

    return total

def part2():
    with open("test.txt", 'r') as file:
        content = file.read()
        separated_content = content.split('\n')

    total = 0
    
    sorted_list = []
    i = len(separated_content[0]) - 1
    while i >= 0:
        temp = ""
        for j in range(len(separated_content)):
            temp += separated_content[j][i]
        sorted_list.append(temp)
        i -= 1

    problems_list = []
    tmp = []
    for i in range(len(sorted_list)):
        if sorted_list[i] != '     ':
            tmp.append(sorted_list[i])
        else:
            problems_list.append(tmp)
            tmp = [] 
    problems_list.append(tmp)

    result_list = []

    for i in range(len(problems_list)):
        tmp2 = []
        for j in range(len(problems_list[i])):
            if problems_list[i][j] != problems_list[i][-1]:
                tmp2.append(int(problems_list[i][j]))
            else:
                tmp2.append(int(problems_list[i][j][:len(problems_list[i][j])-1]))
                tmp2.append(problems_list[i][j][-1])
        result_list.append(tmp2)
        
    for i in range(len(result_list)):
        if result_list[i][-1] == '*':
            result = prod(result_list[i][:len(result_list[i])-1])
            total += result
        elif result_list[i][-1] == '+':
            result = sum(result_list[i][:len(result_list[i])-1])
            total += result
    return total  

if __name__ == "__main__":
    print(part1())
    print(part2())
