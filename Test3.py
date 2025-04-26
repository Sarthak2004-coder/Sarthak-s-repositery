def is_disarium(num):
    sum_digits = 0
    for index, digit in enumerate(str(num), start=1):
        sum_digits += int(digit) ** index
    return sum_digits == num

def first_n_disarium(n):
    result = []
    num = 0
    while len(result) < n:
        if is_disarium(num):
            result.append(num)
        num += 1
    return result

def disarium_between(start, end):
    result = []
    for num in range(start, end + 1):
        if is_disarium(num):
            result.append(num)
    return result

n = int(input())
print(first_n_disarium(n))

start = int(input())
end = int(input())
print(disarium_between(start, end))
