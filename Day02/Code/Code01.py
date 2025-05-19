"""
    数据类型
"""

# 1. 整数int
# -- 十进制
number01 = 18
# -- 二进制
number02 = 0b11
print(number02)
# -- 八进制
number03 = 0o10
print(number03)
# -- 十六进制
number04 = 0x10
print(number04)

# 小整数对象池
a = 500
b = 500
# id(): 返回变量存储的对象地址
print(id(a))
print(id(b))
# Note：在交互式中，两个500不是同一对象。

# 2. 浮点数（小数）float
float01 = 1.0
float02 = 1.23e2
print(float02)

# 3. 字符串str
s01 = "GTX3060TI"
s02 = "3060"
s03 = "3.06"
print("10" +  "2")
print(10 + 2)

# 4. 复数 complex
c01 = 1j
c02 = 5 + 1j
print(c02)
print(type(c02))

# 5. 布尔bool
b01 = True
b02 = False
b03 = 1 > 2
print(b03)

# 6. 数据类型转换
str_score = input("请输入成绩: ")
print(type(str_score))

float_score = float(str_score)
print(type(float_score))