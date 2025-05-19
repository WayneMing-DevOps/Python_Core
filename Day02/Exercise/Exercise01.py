"""
    练习1：在控制台中获取1个变量，再获取1个变量，让两个变量进行交换，然后输出结果。
        变量的交换不是变量的数据交换，实际上交换的内存地址。
"""

# 1. 获取数据
str_input01 = input("Variable1: ")
str_input02 = input("Variable1: ")
print("交换前")
print("Variable1:" + str_input01)
print("Variable2:" + str_input02)

# 2. 利用临时变量进行交换,大部分编程语言通用写法
# str_temp = str_input01
# str_input01 = str_input02
# str_input02 = str_temp

# Python特有的简便写法
str_input01, str_input02 = str_input02, str_input01

# 3. 数据展示
print("交换后")
print("Variable1:" + str_input01)
print("Variable2:" + str_input02)