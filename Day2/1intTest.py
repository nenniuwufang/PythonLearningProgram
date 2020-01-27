def C2F(num):  # 摄氏度转华氏度
    i = eval(num)  # 使用eval()函数对于num进行数值类型的转换
    '''
    此处对于i进行换算，再使用.format()进行格式输出
    '''
    print("{:.2f}".format(i) + 'F\n')


def F2C(num):  # 华氏度转摄氏度
    i = eval(num)  # 使用eval()函数对于num进行数值类型的转换
    '''
    此处对于i进行换算，再使用.format()进行格式输出
    '''
    print("{:.2f}".format(i) + 'C\n')


def main():
    num = input("请输入需要进行转换的温度（xxxC/F）\n")
    # if 'C' in num:
    #     num = num[0:-1]
    #     F2C(num)#如果输入的温度是摄氏度，则将摄氏度转换为华氏度
    # elif 'F' in num:
    #     num = num[0:-1]
    #     F2C(num)#如果输入的温度是华氏度，则将华氏度转换为摄氏度
    # else:
    #     print("输入的数值类型有误，请重新输入")#错误数值的检测，若输入的数值无效，则将错误信息显示
    while True:  # 加入死循环，可以重复使用该分支语句
        if 'C' in num:
            num = num[0:-1]
            F2C(num)  # 如果输入的温度是摄氏度，则将摄氏度转换为华氏度
        elif 'F' in num:
            num = num[0:-1]
            F2C(num)  # 如果输入的温度是华氏度，则将华氏度转换为摄氏度
        elif ' ' in num:
            return 0
        else:
            print("输入的数值类型有误，请重新输入")  # 错误数值的检测，若输入的数值无效，则将错误信息显示
        num = input("请输入需要进行转换的温度（xxxC/F）\n")


if __name__ == '__main__':
    main()  # 温度转换（摄氏度--华氏度）
