from django.shortcuts import render, HttpResponse, redirect, reverse
from web import models


# Create your views here.

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
        i['Companyodds__winalone']=models.Winalone.objects.filter(gameinfo=i['id']).values('homefullwinodds','homefulldefeatodds','fulldrawodds','homehalfwinodds','homehalfdefeatodds','halfdrawodds')
        i['Companyodds__bigsmall']=models.Bigsmall.objects.filter(gameinfo=i['id']).values('big','handicap','small','half_big','half_handicap','half_small')
        i['Companyodds__letball']=models.Letball.objects.filter(gameinfo=i['id']).values('left','Handicap','right','half_left','Half_handicap','half_right')
    # print(all_game)

    print(all_game)
    return render(request,'odds_list.html',{'all_game':all_game})
