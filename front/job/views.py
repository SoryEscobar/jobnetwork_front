from django.shortcuts import render
from django.http import HttpResponse
from front.utilities.request_back_api import BackEndServiceConnection as be_api

# Create your views here.



def job(request):
    
    response = be_api().post('jobs')
    return render(request, 'jobs.html', {"jobs": response['results'], "pagetitle": "Jobs from POST" } )



def job_id(request, jobid):
   
    response = be_api().get(f'jobs/{jobid}')       
    return render(request, 'job.html', {"organization": response['serpTags']['hiringOrganization'],
        "serpTags": response['serpTags'], "attachments":response['attachments'], "response": response, "pagetitle": "Job from GET"})
