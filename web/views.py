from django.shortcuts import render, HttpResponse, redirect, reverse
import time
from web import models


# Create your views here.

def save_excel(path):
    # 打开文件
    data = xlrd.open_workbook(path)
    # 获取sheet名字
    sheet = data.sheet_names()
    # 获取公司信息
    company = data.sheet_by_name(sheet[0]).row_values(0, 1)
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
    # 去除空值
    num = teamname.count([''])
    for n in range(num):
        teamname.remove([''])
    for li in teamname:
        detaild = ''
        for n in range(len(li)):
            if n==len(li)-1:
                detaild = detaild + li[n]
            else:
                detaild=detaild+li[n]+'|'

        models.Teaminfo.objects.create(name=li[0],detaild=detaild)
def odds_list(request):
    '''
    dic={
        event.name={
            time:{}
            info:{}
            full_win_alone{}
            half_win_alone{}
            full_let_ball{}
            half_let_ball{}
            full_big_small{}
        }
    }
    :param request:
    :return:
    '''
    # 队伍信息
    all_game = models.Gameinfo.objects.all().values('id','homename','visitname','gametime','eventid__name','Companyodds__name')
    for i in all_game:
        i['Companyodds__winalone']=models.Winalone.objects.filter(gameinfo=i['id']).values('win','lose','draw','is_half')
        i['Companyodds__bigsmall']=models.Bigsmall.objects.filter(gameinfo=i['id']).values('big','handicap','small','is_half')
        i['Companyodds__letball']=models.Letball.objects.filter(gameinfo=i['id']).values('left','Handicap','right','is_half')
    return render(request,'odds_list.html',{'all_game':all_game})
