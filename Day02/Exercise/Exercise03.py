"""
    在控制台中获取小时/分钟/秒，计算总秒数
"""

# 1. 数据获取
int_Hour = int(input("小时: "))
int_Minute = int(input("分钟: "))
int_Second = int(input("秒: "))

# 2. 逻辑处理
int_Result = int_Hour * 3600 + int_Minute * 60 + int_Second

# 3. 结果输出
print("总秒数: " + str(int_Result))