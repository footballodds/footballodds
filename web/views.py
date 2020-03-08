from django.shortcuts import render, HttpResponse, redirect, reverse
from django.utils import timezone
from django.db.models import Max, Min

import time, datetime, xlrd
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


def workout(a, b, c=None):
    if c == None:
        return round(a * b / (a + b), 4)
    else:
        return round(a * b * c / (a * b + a * c + b * c), 4)


def bigsmall(obj, is_half=0, handicap=None):
    max_odds = {}

    if handicap != None:
        data_all = models.Bigsmall.objects.filter(gameinfo=obj['id'], is_half=is_half, Handicap=handicap).values(
            'companyid__name', 'gameinfo__homename', 'gameinfo__awayname', 'big', 'Handicap', 'small')
        if any(data_all):
            odds = {}
            max_big = data_all.order_by('big').first()
            max_small = data_all.order_by('small').first()
            odds['big'] = max_big
            odds['small'] = max_small
            odds['return_odds'] = workout(max_big['big'], max_small['small'])
            return odds
        else:
            return
    else:
        data = models.Letball.objects.filter(gameinfo=obj['id'], is_half=is_half)
        li = list(set(data.values_list('Handicap')))
        if li:
            for i in li:
                max_odds['handicap'] = letball(obj, is_half=is_half, handicap=i[0])
        else:
            return
    return max_odds


def letball(obj, is_half=0, handicap=None):
    max_odds = {}

    if handicap != None:
        data_all = models.Letball.objects.filter(gameinfo=obj['id'], is_half=is_half, Handicap=handicap).values(
            'companyid__name', 'gameinfo__homename', 'gameinfo__awayname', 'lbleft', 'Handicap', 'lbright')
        if any(data_all):
            odds = {}
            max_lbleft = data_all.order_by('lbleft').first()
            max_lbright = data_all.order_by('lbright').first()
            odds['left'] = max_lbleft
            odds['right'] = max_lbright
            odds['return_odds'] = workout(max_lbleft['lbleft'], max_lbright['lbright'])
            return odds
        else:
            return
    else:
        data = models.Letball.objects.filter(gameinfo=obj['id'], is_half=is_half)
        li = list(set(data.values_list('Handicap')))
        if li:
            for i in li:
                max_odds['handicap'] = letball(obj, is_half=is_half, handicap=i[0])
        else:
            return
    return max_odds


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
        max_odds['return_odds'] = workout(max_win['win'], max_draw['draw'], max_lose['lose'])
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
            i['winodds'] = winodds(i)
            i['half_winodds'] = winodds(i, is_half=1)
            i['letball'] = letball(i)
            i['half_letball'] = letball(i, is_half=1)
            i['bigsmall'] = bigsmall(i)
            i['half_bigsmall'] = bigsmall(i, is_half=1)
            if i['letball']!=None:
                    print('让球',i['letball']['handicap']['return_odds'])
                    if i['letball']['handicap']['return_odds']>=1:
                        print(i)
            if i['half_letball']!=None:
                if i['half_letball']['handicap']['return_odds']>=1:
                    print(i)

            if i['bigsmall']!=None :
                print('大小',i['bigsmall']['handicap']['return_odds'])
                if i['bigsmall']['handicap']['return_odds']>=1:
                    print(i)

            if i['half_bigsmall']!=None :
                if i['half_bigsmall']['handicap']['return_odds']>=1:
                    print(i)

    return render(request, 'odds_list.html', {'all_game': all_game})
