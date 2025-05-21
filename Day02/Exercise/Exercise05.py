# 闰年判断:
# 条件1:  年份能被4整除,但是不能被100整除.
# 条件2:  年份能被400整除
# 在控制台中获取年份
# 判断是否为闰年,如果是显示true,否则显示false

int_Year = int(input("请输入年: "))
result = (int_Year % 4 == 0 and int_Year % 100 != 0) or (int_Year % 400 == 0)
print(result)
# if (int_Year % 4 == 0 and int_Year % 100 != 0) or (int_Year % 400 == 0):
#     print("true")
# else:
#     print("false")
