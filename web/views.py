from django.shortcuts import render, HttpResponse, redirect, reverse
from django.utils import timezone
from django.db.models import Max, Min

import time, datetime
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
            if n == len(li) - 1:
                detaild = detaild + li[n]
            else:
                detaild = detaild + li[n] + '|'

        models.Teaminfo.objects.create(name=li[0], detaild=detaild)


def bigsmall(obj, is_half=0):
    pass


def letball(obj, is_half=0,handicap=None):
    max_odds = {}

    if handicap!=None:
        data_all = models.Letball.objects.filter(gameinfo=obj['id'], is_half=is_half,Handicap=handicap).values('companyid__name','gameinfo__homename','gameinfo__awayname', 'lbleft','Handicap','lbright')
        if any(data_all):
            odds={}
            max_lbleft=data_all.order_by('lbleft').first()
            max_lbright=data_all.order_by('lbright').first()
            odds['left']=max_lbleft
            print(odds)
            return odds
        else:
            return
    else:
        data = models.Letball.objects.filter(gameinfo=obj['id'], is_half=is_half)
        li=list(set(data.values_list('Handicap')))
        if li:
            for i in li:
                max_odds['handicap']=letball(obj,is_half=is_half,handicap=i[0])
        else:
            return
    return max_odds
    # if any(data_all):
    #     print(list(set(data_all)))


def winodds(obj, is_half=0):
    max_odds = {}
    data_all = models.Winalone.objects.filter(gameinfo=obj['id'], is_half=is_half).values('companyid__name',
                                                                                          'gameinfo__homename',
                                                                                          'gameinfo__awayname', 'win',
                                                                                          'draw', 'lose')
    if any(data_all):
        max_win = data_all.order_by('-win').first()
        max_draw = data_all.order_by('-draw').first()
        max_lose = data_all.order_by('-lose').first()
        max_odds['win'] = [max_win['companyid__name'], max_win['gameinfo__homename'], max_win['win']]
        max_odds['draw'] = [max_draw['companyid__name'], '平局', max_draw['draw']]
        max_odds['lose'] = [max_lose['companyid__name'], max_win['gameinfo__awayname'], max_lose['lose']]
        max_odds['return_odds'] = max_win['win'] * max_draw['draw'] * max_lose['lose'] / (
                max_win['win'] * max_draw['draw'] + max_draw['draw'] * max_lose['lose'] + max_win['win'] * max_lose[
            'lose'])
        max_odds['return_odds'] = round(max_odds['return_odds'], 4)
    else:
        return
    return max_odds


def odds_list(request):
    '''
    :param request:
    :return:
    '''
    # 联赛信息：
    all_event = models.Eventinfo.objects.all().values('id', 'name')
    all_game = {}
    now = timezone.now()
    for all in all_event:
        # 队伍信息
        all_gameinfo = models.Gameinfo.objects.filter(eventid=all['id'], gametime__gt=now).values('id', 'homename',
                                                                                                  'awayname',
                                                                                                  'gametime',
                                                                                                  'eventid__name',
                                                                                                  'Companyodds__name')
        all_game[all['name']] = all_gameinfo
        for i in all_gameinfo:
            # i['Companyodds__winalone'] = models.Winalone.objects.filter(gameinfo=i['id']).values('win', 'draw', 'lose',
            #                                                                                      'is_half',
            #                                                                                      'companyid__name')
            # i['Companyodds__bigsmall'] = models.Bigsmall.objects.filter(gameinfo=i['id']).values('big', 'handicap', 'small',
            #                                                                                      'is_half',
            #                                                                                      'companyid__name')
            # i['Companyodds__letball'] = models.Letball.objects.filter(gameinfo=i['id']).values('lbleft', 'Handicap',
            #                                                                                    'lbright', 'is_half',
            #
            #                                                                                   'companyid__name')
            i['letball'] = letball(i)
            i['winodds'] = winodds(i)
            i['half_winodds'] = winodds(i, is_half=1)

    return render(request, 'odds_list.html', {'all_game': all_game})
