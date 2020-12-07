from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from front.utilities.request_back_api import BackEndServiceConnection as be_api


# Create your views here.


def default(request):
    return HttpResponse('<p>The fontend is online!</>')
    
        

def user(request):
    users = be_api().post('user')
    return render(request, 'users.html', {"users": users['results'], "pagetitle": "Users from POST"})
