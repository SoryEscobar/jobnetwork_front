from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from front.utilities.request_back_api import BackEndServiceConnection as be_api


# Create your views here.


def default(request):
    #return HttpResponse('<p>The fontend is online!</>')
    return redirect('/users')
    
        

def user(request):
    users = be_api().post('users')
    return render(request, 'users.html', {"users": users['results'], "pagetitle": "Users from POST"})


def user_id(request, username=None):
    user = be_api().get(f'users/{username}')
    return render(request, 'user.html', {"person": user['person'], "stats": user['stats'], "pagetitle": "User from GET"})
