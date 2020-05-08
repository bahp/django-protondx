from django.urls import include, path
from rest_framework import routers

from . import views
from . import api_viewsets

router = routers.DefaultRouter()
router.register('patients', api_viewsets.PatientViewSet)
router.register('testing-centres', api_viewsets.TestingCentreViewSet)
router.register('diagnostic-tests', api_viewsets.DiagnosticTestViewSet)
# router.register('popup', api_viewsets.PopupViewSet, basename='Popup')

app_name = 'dashboard'
urlpatterns = [

    # Dashboard
    # <IP>/dashboard/
    path('', views.DashView.as_view(), name='dash'),

    # API
    path('api/', include(router.urls)),
]

