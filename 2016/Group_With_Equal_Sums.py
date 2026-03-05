def equal_sum_list():
    numbers = []
    for _ in range(4):
        numbers.append(int(input()))
    total_sum = sum(numbers)
    if total_sum % 2 != 0:
        print("No")
        return

    target = total_sum // 2
    found = False
    for i in range (4):
        if numbers[i] == target:
            found = True
            break
    if not found:
        for i in range (4):
            for j in range(i + 1, 4):
                if numbers[i] + numbers[j] == target:
                    found = True
                    break
            if found: break
    if found:
        print("Yes")
        print(target)
    else:
        print("No")
equal_sum_list()

