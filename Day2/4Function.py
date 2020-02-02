'''
函数（项目）
函数的复用（绘画科赫曲线）

使用关键字def来对函数进行定义
def ____[函数名称]:
# 命名规则：
    1.对于函数、变量、常量我们通常会对其进行命名
    2.命名可以使用数字、英文、下划线甚至中文(utf-8)
    3.命名开头只能以英文、中文汉字开头，下划线不可以打头使用
# 正确的命名:
    helloworld
    Hi_Luoyang
    r3tr0
    this_is_a_varible
    你好洛阳 = 'helloworld'
    ……………………
# 错误的命名：
    3dsll
    _helloPython
# 大小驼峰命名法……

对于项目而言，最重要的是IPO
I:Input 输入
P:Progress 处理
O:Output 输出
对于程序的功能我们一般使用“函数”对其进行定义封装使用
常量与变量
实参与形参
'''
import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)
            # 在此处 函数自己调用了自己 此为函数的复用
            # 同时 函数也需要一个结束的条件来结束函数的自我调用


def main():
    # 函数名为main的函数 一般称为主函数
    # 在其他编程语言中 main函数一般缺一不可
    # 且有且仅有一个main()函数
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(5)
    turtle.pencolor("pink")
    level = 3
    for i in range(3):
        koch(400, 3)
        turtle.right(120)
    turtle.hideturtle()


if __name__ == '__main__':
    main()
