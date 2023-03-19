
def get_even_numbers(begin, end):
    even_list = []
    for num in range(begin, end):
        if num % 2 == 0:
            even_list.append(num)
    return even_list


begin = 4
end = 15
print(f"begin = {begin},end = {end},even numbers:", get_even_numbers(begin, end))

# 列表推导式
data = [item for item in range(begin,end) if item % 2 ==0]
print(f"begin = {begin},end = {end},even numbers:", data)