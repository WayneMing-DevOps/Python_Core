"""
    5.修改exercise03中的练习,如果金额不足,提示还差多少钱,如果金额够,提示应找回多少钱.
    -- 尝试:如果总价到达100元,打八折.
"""
# 1. 获取数据
str_Unit_Price = input("商品单价: ")
float_Price = float(str_Unit_Price)

int_Unit_Number = int(input("商品数量: "))
float_Amount = float(input("获取金额: "))

# 2. 逻辑处理
float_Result = float_Amount - (float_Price * int_Unit_Number)

if float_Amount >= 100:
    float_Amount *= 0.8

# 3. 输出结果
if float_Result < 0:
    print("还差:" + str(float_Amount - float_Result))
else:
    print("应找回金额: " + str(float_Result))

