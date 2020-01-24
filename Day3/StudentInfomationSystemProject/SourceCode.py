# def exit():
#     # 输入0调用

def insert():
    # 输入1调用 录入学生信息
    pass

def search():
    # 输入2调用 查找学生信息
    pass

def delete():
    # 输入3调用 删除学生信息
    pass

def modify():
    # 输入4调用 修改学生信息
    pass

def sort():
    # 输入5调用 对学生以成绩的高低进行排序
    pass

def total():
    # 输入6调用 统计学生总人数
    pass

def showInfo():
    # 输入7调用 显示所有学生信息
    pass

def menu():
    print("学生信息管理系统")
    print("1.录入学生信息")
    print("2.查找学生信息")
    print("3.删除学生信息")
    print("4.修改学生信息")
    print("5.对学生以成绩的高低进行排序")
    print("6.统计学生总人数")
    print("7.显示所有学生信息")
    print("0.退出系统")

def main():
    flg = True
    while flg:
        menu()
        Op = eval(input("请输入您要进行操作的序号"))
        if Op == 1:
            insert()
        elif Op == 2:
            search()
        elif Op == 3:
            delete()
        elif Op == 4:
            modify()
        elif Op == 5:
            sort()
        elif Op == 6:
            total()
        elif Op == 7:
            showInfo()
        elif Op == 0:
            print("您已经退出学生管理系统！期待您的下次使用！")
            break
if __name__ == '__main__':
    main()