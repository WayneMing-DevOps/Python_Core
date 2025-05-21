"""
    在控制台中获取一个总秒数
    计算几小时零几分钟零几秒钟.
"""

int_Second = int(input("请输入总秒数:"))

int_Hour = int_Second // 3600
int_Minute = int_Second // 60 % 60
int_Second_Re = int_Second % 60

print(str(int_Hour) + "小时" + str(int_Minute) + "分钟" + str(int_Second_Re) + "秒")
