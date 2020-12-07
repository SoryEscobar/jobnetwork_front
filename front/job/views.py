from django.shortcuts import render
from django.http import HttpResponse
from front.utilities.request_back_api import BackEndServiceConnection as be_api

# Create your views here.



def job(request):
    #Make the API request
    
    response = be_api().post('job')
    return render(request, 'jobs.html', {"jobs": response['results'], "pagetitle": "Jobs from POST" } )
