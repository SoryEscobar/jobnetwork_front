from django.urls import path
from job import views

urlpatterns = [
    path('',                views.job, name="Job"),
]
