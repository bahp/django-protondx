from django.urls import include, path
from rest_framework import routers

from . import views
from . import api_viewsets

router = routers.DefaultRouter()
router.register('patients', api_viewsets.PatientViewSet)
router.register('testing-centres', api_viewsets.TestingCentreViewSet)
#router.register('diagnostic-tests', api_viewsets.DiagnosticTestViewSet)

app_name = 'dashboard'
urlpatterns = [

    # Dashboard
    # <IP>/dashboard/
    path('', views.DashView.as_view(), name='dash'),
    path('api/diagnostic-tests/', api_viewsets.DiagnosticTestViewSet.as_view()),
    path('api/get-postcode-data/', api_viewsets.PostcodeData.as_view()),
    # API
    path('api/', include(router.urls)),
]

