# MainFilePath
# open("./stuInfo.txt", "r", encoding="utf-8")
# SourceCode.py
# 请在函数的相应位置(pass处)填写相对应函数功能的代码以完成整个学生信息管理系统的项目
# 具体的菜单函数以及save()函数均已经给出。
"""
学生信息：
{"Sid":Sid,"Sname":Sname,"Sage":Sage,"ChineseScore":ChineseScore,"MathScore":MathScore,"EnglishScore":EnglishScore}
"""


def save(studentInfo):
    try:
        stuFile = open("./stuInfo.txt", "a", encoding="utf-8")  # 若文件存在 追加写
    except Exception as e:
        stuFile = open("./stuInfo.txt", "w", encoding="utf-8")  # 若文件不存在 创建文件覆盖写
    for info in stuFile:
        stuFile.write(str(info) + "\n")  # 按行写入文件stuInfo.txt中
    stuFile.close()  # 关闭文件


def insert():
    pass


def search():
    pass


def delete():
    pass


def modify():
    pass


def sort():
    pass


def total():
    pass


def show():
    pass


def menu():
    print("欢迎使用学生信息管理系统\n"
          "0.退出系统\n"  # exit()
          "1.插入学生数据\n"  # insert()
          "2.查询学生数据\n"  # search()
          "3.删除学生数据\n"  # delete()
          "4.修改学生数据\n"  # modify()
          "5.按成绩对学生排序\n"  # sort()
          "6.统计学生总人数\n"  # total()
          "7.显示全部学生信息\n")  # show()
    # menu()


def main():
    while True:
        menu()
        op = eval(input("请输入您所需要的操作(0~7)"))
        if op == 0:
            control = input("您确定退出学生信息管理系统?(y/n)")
            if control in ["y", "y"]:
                print("您已成功退出学生信息管理系统！")
                break
            elif control in ["n", "N"]:
                print("欢迎继续使用学生信息管理系统！")
                continue
        elif op == 1:
            insert()
        elif op == 2:
            search()
        elif op == 3:
            delete()
        elif op == 4:
            modify()
        elif op == 5:
            sort()
        elif op == 6:
            total()
        elif op == 7:
            show()
        menu()
        op = eval(input("请输入您所需要的操作(0~7)"))


if __name__ == '__main__':
    main()
