# coding=utf-8

import xlrd, time


# from web import models
class matchinfo:

    def __init__(self, matchname, teamname, company):
        self.matchname = matchname
        self.teamname = teamname
        self.company = company


# 打开文件
data = xlrd.open_workbook('C:/Users/Administrator/Desktop/TeamName.xls')

# 查看工作表
sheet = data.sheet_names()

company = data.sheet_by_name('奥甲').row_values(0, 1)
print(company, round(time.time() * 1000))

# 通过文件名获得工作表,获取工作表1
matchname = []
teamname = []
for i in sheet:
    table = data.sheet_by_name(i)
    li = table.row_values(2, 1)
    matchname.append(li)
    for n in range(4, 8):
        if table.cell(n, 2) == '':
            continue
        teamname.append(list(set(table.row_values(n, 1))))

print('联赛', matchname[0:-3])
num=teamname.count([''])
for n in range(num):
    teamname.remove([''])

print('队伍', teamname)

# 打印data.sheet_names()可发现，返回的值为一个列表，通过对列表索引操作获得工作表1
# table = data.sheet_by_index(0)

# 获取行数和列数
# 行数：table.nrows
# 列数：table.ncols


# 获取整行的值 和整列的值，返回的结果为数组
# 整行值：table.row_values(start,end)
# 整列值：table.col_values(start,end)
# 参数 start 为从第几个开始打印，
# end为打印到那个位置结束，默认为none
#     print("整行值：" + str(table.row_values(0)))
#     print("整列值：" + str(table.col_values(1)))

# 获取某个单元格的值，例如获取B3单元格值
#     cel_B3 = table.cell(3,2).value
#
