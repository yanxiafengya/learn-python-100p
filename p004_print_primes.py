#
# def is_primes(number):
#     num = 0
#     for i in range(1, number+1):
#         # print(i)
#         if number % i ==0:
#             num += 1
#     if num == 2:
#         return True
#     else:
#         return False

def is_primes(number):
    if number == 1:
        return False
    if number ==2:
        return True
    for idx in range(2,number):
        if number % idx == 0:
            return False

    return True


def print_primes(begin, end):
    for num in range(begin, end + 1):
        if is_primes(num):
            print(f"{num} is a prime")


begin = 1
end = 1
print_primes(begin, end)
