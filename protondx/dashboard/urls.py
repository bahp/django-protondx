"""
This module contains the URL configuration settings for the Dashboard App
"""

from django.urls import include, path
from rest_framework import routers

from . import views
from . import api_viewsets

# Router for Django REST API URLs
router = routers.DefaultRouter()
router.register('patient', api_viewsets.PatientViewSet)
router.register('testing-centre', api_viewsets.TestingCentreViewSet)

app_name = 'dashboard'
urlpatterns = [

    # Dashboard
    # <IP>/dashboard/
    path('', views.DashView.as_view(), name='dash'),

    # ---------------
    # Django REST API
    # ---------------

    # Routers
    path('api/', include(router.urls)),

    # Custom
    path('api/get-postcode-data/', api_viewsets.PostcodeData.as_view()),
    path('api/get-points/', api_viewsets.GeoView.as_view()),
    path('api/diagnostic-test/', api_viewsets.DiagnosticTestView.as_view()),
    path('api/diagnostic-detail/', api_viewsets.DiagnosticDetailView.as_view()),

]
