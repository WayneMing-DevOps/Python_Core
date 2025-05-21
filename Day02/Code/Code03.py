"""
    逻辑运算符
    身份运算符
"""
# and
print(True and True)
print(False and False)
print(True and False)

# or
print(True or True)
print(False or False)
print(True or False)
print(False or True)
print(1 > 2 or 5 < 3 or 10 > 5)

# 短路逻辑
# 如果第一个条件不满足，则不再考虑第二个条件
# 建议：尽量将耗时的判断，放在后面，因为很有可能不执行！

# 身份运算符
num01 = 800
num02 = 900
num03 = num01
print(num01 is num02)
print(id(num01) == id(num02))
print(num03 is num01)