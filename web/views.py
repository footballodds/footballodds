from django.shortcuts import render,HttpResponse,redirect,reverse
from web import models
# Create your views here.

def odds_list(request):
    '''
    dic={
        event.name={
            time:{}
            info:{}
            odd{}
        }
    }
    :param request:
    :return:
    '''

    all_event=models.Eventinfo.objects.all().values()
    print([models.Gameinfo.objects.filter(eventid=i['id']).values() for i in all_event])
    return HttpResponse('ok')