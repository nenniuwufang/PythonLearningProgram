# 字典的使用规范
# 字典的结构：
# 字典的结构一般为{key：value}的形式
# 调用key会返回value的值 value的值可以限定为默认值

dict = {"name": "小明", "age": 20, "sex": "male"}
# 此为字典的赋值方式
i = dict.get("name")
# 此为获取字典key后值的形式之一
# 该方法不对字典本身做出任何更改
print(i)
print(dict)
j = dict.pop("name")
# 此为获取键名称为“name”的值的形式之二
# 该方法会对于字典本身造成更改
"""
具体的更改方式为：
为将名为“name”的键与键所对应的值取出并将键所对应的值返回 在将该键与键值删除
"""
print(j)
print(dict)  # 打印已经更改过后的字典
