from django.shortcuts import render
from django.http import HttpResponse
from .utils.request_back_api import BackEnd as be


# Create your views here.


def default(request):
    return HttpResponse('<p>The fontend is online!</>')
    
        

def user(request):
    #TODO: Fix this render
    #TODO: Connect this to the API
    
    users = be().get_user()

    return HttpResponse(users)
