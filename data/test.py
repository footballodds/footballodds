# 一个类
# 对象的属性 : 姓名 性别 年龄 部门
# 员工管理系统
# 内部转岗 python开发 - go开发
# 姓名 性别 年龄 新的部门
# alex None 83 python
# alex None 85 luffy

# 1000个员工
# 如果几个员工对象的姓名和性别相同,这是一个人
# 请对这1000个员工做去重

class Employee:
    def __init__(self,name,age,sex,partment):
        self.name = name
        self.age = age
        self.sex = sex
        self.partment = partment
    def __hash__(self):
        return hash('%s%s'%(self.name,self.sex))
    def __eq__(self, other):
        if self.name == other.name and self.sex == other.sex:
            return True
employ_lst = []
for i in range(200):
    employ_lst.append(Employee('alex',i,'male','python'))
for i in range(200):
    employ_lst.append(Employee('wusir',i,'male','python'))
for i in range(200):
    employ_lst.append(Employee('taibai', i, 'male', 'python'))

# print(employ_lst)
employ_set = set(employ_lst)
for person in employ_set:
    print(person.__dict__)

# set集合的去重机制 : 先调用hash,再调用eq,eq不是每次都触发,只有hash值相等的时候才会触发