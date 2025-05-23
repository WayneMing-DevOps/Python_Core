"""
    在控制台中获取圆形的半径
   计算面积(3.14 * r 的平方)与周长(2 * 3.14 * r)
"""

# 1. 数据获取
str_Radius = input("圆形半径: ")

# 2. 逻辑处理
float_Area = round(3.14 * float(str_Radius), 2)
float_Perimeter = round(2 * 3.14 * float(str_Radius), 2)

# 3. 结果输出
print(float_Area, float_Perimeter)