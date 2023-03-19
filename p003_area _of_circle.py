import math
# print(math.pi)


def computer_area_of_circle(r):
    # 保留两位小数 round函数
    return round(math.pi * r * r, 2)


if __name__ == '__main__':
    print("area of 2 is:", computer_area_of_circle(2))
    print("area of 3.14 is:", computer_area_of_circle(3.14))
    print("area of 6.78 is:", computer_area_of_circle(6.78))
