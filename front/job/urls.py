from django.urls import path
from job import views

urlpatterns = [
    path('',                views.job, name="Job"),
    path('<jobid>/',        views.job_id, name="job_specific"),
]
