"""
    古代的称一斤16两。
    在控制台中获取两，换算出是几斤几两。
"""
# 1. 获取数据
int_Total_Liang = int(input("请输入两: "))

# 2. 逻辑处理
int_Jin = int_Total_Liang // 16
int_Liang = int_Total_Liang % 16

# 3. 数据展示
print(str(int_Jin) + "斤零" + str(int_Liang) + "两")
