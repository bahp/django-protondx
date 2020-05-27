from django.urls import path
from . import views, api_viewsets


app_name = 'dataUpload'
urlpatterns = [

    # Data Upload page
    # <IP>/dataUpload/
    path('', views.dataUploadView, name='dataUpload'),

    # ---------------
    # Django REST API
    # ---------------
    # path('api/sample-poster/', api_viewsets.sample_poster, name='sample_poster'),
]
