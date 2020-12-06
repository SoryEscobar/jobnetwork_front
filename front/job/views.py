from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def job(request):
    return HttpResponse('<h2>Job endpoint working</h2>')
