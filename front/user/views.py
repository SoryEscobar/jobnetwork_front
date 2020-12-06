from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from .utils.request_back_api import BackEnd as be


# Create your views here.


def default(request):
    return HttpResponse('<p>The fontend is online!</>')
    
        

def user(request):
    users = be().get_user()
    return render(request, 'user_view/home.html', {"users": users['results']})
