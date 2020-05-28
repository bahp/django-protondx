from django.urls import path
from . import views


app_name = 'dataUpload'
urlpatterns = [

    # Data Upload page
    # <IP>/dataUpload/
    path('', views.dataUploadView, name='dataUpload'),

]
