from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    # <IP>/dashboard/
    path('', views.DashView, name='dash'),
]
