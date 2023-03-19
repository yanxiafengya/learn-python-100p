

def sum_of_square(num):
    result = 0
    for i in range(1, num+1):
        result += i * i
    return result


print(sum_of_square(3))
print(sum_of_square(5))
print(sum_of_square(10))

