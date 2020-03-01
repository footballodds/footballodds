from django.shortcuts import render,HttpResponse,redirect,reverse
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

    all_event=models.Eventinfo.objects.all().values()

    print([models.Gameinfo.objects.filter(eventid=i['id']).values() for i in all_event])
    return HttpResponse('ok')