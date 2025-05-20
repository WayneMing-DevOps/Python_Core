"""
    在控制台中获取一个商品单价，再获取一个商品数量，再获取一个金额。
        计算：应该找回多少钱
"""

# 1. 获取数据
str_Unit_Price = input("商品单价: ")
float_Price = float(str_Unit_Price)

int_Unit_Number = int(input("商品数量: "))
float_Amount = float(input("获取金额: "))

# 2. 逻辑处理
# float_Price, float_Number, float_Amount = float(str_Price), float(str_Number), float(str_Amount)
float_Result = float_Amount - (float_Price * int_Unit_Number)

# 3. 输出结果
print("应找回金额: " + str(float_Result))