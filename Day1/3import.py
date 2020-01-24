import math # 调用数学库
# from math import pi

def main():# 计算圆的面积
    r = eval(input("请输入待求圆的半径")) # input()输入圆的半径 并对输入的字符串进行格式转换(eval())
    SquareR = pow(r,2)
    # pow()函数为幂计算所用 其中pow(a,b)代表的是a的b次幂
    # pow(Exp,x)->e^x
    S = SquareR * math.pi
    # 此处的math.pi为精度很高的常数 存放在math库中
    # S = math.pi*r*r
    # print(S)
    print("{:.2f}".format(S))

if __name__ == '__main__':
    main()# 调用库的练习