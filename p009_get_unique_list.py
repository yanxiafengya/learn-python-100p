
def get_unique_list(lista):
    result = []
    for item in lista:
        if item not in result:
            result.append(item)
    return result

lista = [10, 20, 30, 10, 20]
print(f"source list {lista},unique list:", get_unique_list(lista))
# set集合内不会有重复元素
print(f"source list {lista},unique list:", list(set(lista)))
print(f"source list {lista},unique list:", set(lista)) #集合