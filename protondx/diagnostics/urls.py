# Generic
from django.urls import path, include
from django.views.generic.base import TemplateView

# Rest framework
from rest_framework import routers
from rest_framework.authtoken import views as drf_views
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

# App libraries
from . import views
from . import api_viewsets

# -----------------------------------
# Create a router with the URLs.
# -----------------------------------
# Create a router with the URLs.
router = routers.DefaultRouter()
router.register('device', api_viewsets.DeviceViewSet)
router.register('cartridge', api_viewsets.CartridgeViewSet)
router.register('experiment', api_viewsets.ExperimentViewSet)
#router.register('summary', api_viewsets.SummaryExperimentViewSet)

# ----------------------------------
# Define url patterns
# ----------------------------------
urlpatterns = [
    # Add the API
    path('api/', include(router.urls)),

    path('api/summary/count', api_viewsets.SummaryExperimentViewSet.as_view()),
]