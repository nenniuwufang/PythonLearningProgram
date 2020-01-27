"""
if（条件）:
elif（条件）:
else（没有条件）:
分支
###########################################################################
for（条件）:
else（没有条件）:

while（条件）:
else（没有条件）:
循环
"""


# def main():
#
#     word = input("请输入有待输出的数字类型")# 输入有待输出的字符类型
#     i = input("请输入有待转换的字符")
#
#     if word == "str":
#         i = str(i)
#         print(type(i))
#         print(i)
#     elif 'num' in word:
#         if "int" in word:
#             i = int(i)
#             print(type(i))
#             print(i)
#         elif "float" in word:
#             i = float(i)
#             print(type(i))
#             print(i)
#         else:
#             i = '暂无该数字类型！'
#             print(i)
#
# if __name__ == '__main__':
#     main()#字符转换 分支练习

###########################################################################

def main():
    # for i in range(100):
    # for i in list():
    # for i in str():
    # else:(当且仅当完成了全部for循环后执行)
    # for i in range(10):
    #     print(i)
    str = 'helloworld'
    for i in str:
        if i == 'o':
            # break 跳出循环
            # continue 再进行一次循环
            # break
            continue
        print(i, end='')
        # end=''代表的是结尾无空格输出
    else:
        print("运行成功")


if __name__ == '__main__':
    main()  # 循环练习

# def main():
#     a = eval(input("请输入a的值"))
#
#     if a == 1 and a != -1:
#     # 双目运算符 即两个相连的符号
#     # 单个等号（=）为赋值 双等号（==）为比较 此时的双引号比较为判断该值是否和等号后的值相等
#     # 此外 感叹号加等号（！=）必须相连 表示不等于
#         print("True")
#     elif a == -1:
#         print("-1")
#     else:
#         print("False")
#
# if __name__ == '__main__':
#     main()
