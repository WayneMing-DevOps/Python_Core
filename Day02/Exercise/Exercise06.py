#练习2: 在控制台中获取一个4位整数1234
#    计算每位相加和  1+2+3+4  -->  10

int_Unit_Number = int(input("请输入4位整数: "))

int_One = int_Unit_Number // 1000
int_Two = int_Unit_Number % 1000 // 100
int_Three = int_Unit_Number % 100 // 10
int_four = int_Unit_Number % 10
int_Result = int_One + int_Two + int_Three + int_four

print("Result: " + str(int_Result))