def sum_of_list(param_list):
    result = 0
    for number in param_list:
        result += number
    return result
# 格式化的快捷键是：ctrl +alt+L


list1 = [1, 2, 3, 4]
list2 = [17, 5, 3, 5]

print(f"the sum of {list1}is ：{sum_of_list(list1)}")
print(f"the sum of {list2}is ：", sum_of_list(list2))

print(f"the sum of {list1}is ：{sum(list1)}")
print(f"the sum of {list2}is ：", sum(list2))
