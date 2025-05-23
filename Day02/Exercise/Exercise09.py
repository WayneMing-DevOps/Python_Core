"""
    温度换算器(华氏度,摄氏度,开氏度)
    摄氏度 = (华氏度 - 32) / 1.8
    华氏度 = 摄氏度*1.8 + 32
    开氏度 = 摄氏度 + 273.15
    -- 在控制台中获取华氏度,计算摄氏度
    -- 在控制台中获取摄氏度,计算华氏度
    -- 在控制台中获取摄氏度,计算开氏度
"""
# 1. 数据获取
float_Number1_H = float(input("请输入华氏度: "))
float_Number2_S = float(input("请输入摄氏度: "))
float_Number3_K = float(input("请输入摄氏度: "))

# 2. 逻辑处理
float_Number1_H = (float_Number1_H - 32) / 1.8
float_Number2_S = float_Number2_S * 1.8 + 32
float_Number3_K = float_Number3_K + 273.15

# 3. 结果输出
print(float_Number1_H, float_Number2_S, float_Number3_K)
