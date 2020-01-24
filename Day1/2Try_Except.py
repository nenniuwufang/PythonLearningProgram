"""
try:
    ___
except___:
#ZeroDivisionError#
#NameError#
#ValueError#

####################################################

try:
    ___
except___:
    ___
except:
    ___
else:
    ___
finally:
    ___
"""

try:
    # print(1/1)
    # print(0 / 0)
    a = 0/0
except ZeroDivisionError:
    print("除0错误！")
except:
    print("其他错误！")
else:
    print("没有错误！")
finally:
    print("程序执行完毕！")
