from django.urls import path
from user import views

urlpatterns = [
    path('',                views.user, name="User"),
    path('<username>/',           views.user_id, name="user_specific"),
]
