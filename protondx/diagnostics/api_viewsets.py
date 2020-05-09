# Django libraries
from django.template import loader
from django.utils import timezone
from django.views import generic
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


# Django rest framework
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.renderers import JSONRenderer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Django filters
from django_filters.rest_framework import DjangoFilterBackend

"""
# Django rest framework bulk
from rest_framework_bulk import BulkModelViewSet
from rest_framework_bulk import ListBulkCreateAPIView
"""

# Models
from . import models
from . import api_serializers as serializers
from . import api_filters as filters


# -----------------------
# Clinician view
# -----------------------
class DeviceViewSet(viewsets.ModelViewSet):
    """This class handles the API device requests.

    retrieve:
        Returns a device instance.

    list:
        Return all device, ordered by most recent (date_created).

    create:
        Create a new device.

    delete:
        Remove an existing device.

    partial_update:
        Update one or more fields on an existing clinician.

    update:
        Update a clinician
    """   
    # -------
    # Basic
    # -------
    # Basic configuration
    queryset = models.Device.objects.all()
    serializer_class = serializers.DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]
    #pagination_class = DynamicPageNumberPagination

    # -------
    # Filters
    # -------
    # Filters
    #search_fields = ('comments', )
    filter_fields = '__all__'
    ordering_fields = '__all__'

    # Set backends
    filter_backends = (DjangoFilterBackend, 
                       SearchFilter,
                       OrderingFilter)

    # Enable further filtering
    #filter_class = 

    # Define default ordering
    ordering = ('-date_created', )

# -----------------------
# Patient view
# -----------------------
class CartridgeViewSet(viewsets.ModelViewSet):
    """This class handles the API cartridge requests.

    retrieve:
        Returns a cartridge instance.

    list:
        Return all cartridges, ordered by most recent (date_created).

    create:
        Create a new cartridge.

    delete:
        Remove an existing patient.

    partial_update:
        Update one or more fields on an existing cartridge.

    update:
        Update a case.
    """   
    # -------
    # Basic
    # -------
    # Basic configuration
    queryset = models.Cartridge.objects.all()
    serializer_class = serializers.CartridgeSerializer
    permission_classes = [permissions.IsAuthenticated]
    #pagination_class = DynamicPageNumberPagination

    # -------
    # Filters
    # -------
    # Filters
    #search_fields = ('comments', )
    filter_fields = '__all__'
    ordering_fields = '__all__'

    # Set backends
    filter_backends = (DjangoFilterBackend, 
                       SearchFilter,
                       OrderingFilter)

    # Enable further filtering 
    #filter_class = 

    # Define default ordering
    ordering = ('-date_created', )



# -----------------------
# Case view
# -----------------------
class ExperimentViewSet(viewsets.ModelViewSet):
    """This class handles the API case requests.

    retrieve:
        Returns a case instance.

    list:
        Return all cases, ordered by most recent (date_created).

    create:
        Create a new case.

    delete:
        Remove an existing case.

    partial_update:
        Update one or more fields on an existing case.

    update:
        Update a case.
    """     
    # -------
    # Basic
    # -------
    # Basic configuration
    queryset = models.Experiment.objects.all()
    serializer_class = serializers.ExperimentSerializer
    permission_classes = [permissions.IsAuthenticated]
    #pagination_class = DynamicPageNumberPagination

    # -------
    # Filters
    # -------
    # Filters
    #search_fields = ('comments', )
    filter_fields = '__all__'
    ordering_fields = '__all__'

    # Set backends
    filter_backends = (DjangoFilterBackend, 
                       SearchFilter,
                       OrderingFilter)

    # Enable further filtering 
    #filter_class = 

    # Define default ordering
    ordering = ('-date_created', )




class SummaryViewSet(generics.ListAPIView):
    """This class returns a summary of the experiment tests.

    """     
    # -------
    # Basic
    # -------
    # Basic configuration
    queryset = models.Experiment.objects.all()
    serializer_class = serializers.ExperimentSerializer
    #serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    #pagination_class = DynamicPageNumberPagination

    # -------
    # Filters
    # -------
    # Filters
    search_fields = ('disease', )
    filter_fields = '__all__'
    ordering_fields = '__all__'
    #filterset_fields equality filter

    # Set backends
    filter_backends = (DjangoFilterBackend, 
                       SearchFilter,
                       OrderingFilter)

    # Enable further filtering 
    #filter_class = 

    # Define default ordering
    ordering = ('-date_created', )


    def list(self, request, *args, **kwargs):
        """This method lists and adds count summary.

        .. note: In order to count groups properly, it needs order_by.

        .. todo: Find a generic approach for the case of choice field to
                 translate the code (e.g. MALARIA) to the display name
                 (e.g. Malaria). Remember that the method used for display
                 is get_<attribute>_display(). 

                 see: https://stackoverflow.com/questions/23693631/get-full-label-name-of-choicefield-in-queryset-values-list
        """
        response = super().list(request, args, kwargs)
        # Get attribute from model to count by
        attribute = self.request.query_params.get('by', None)
        # Group count
        if attribute:
            smry = self.filter_queryset(self.queryset) \
                       .values(attribute) \
                       .annotate(count=Count(attribute)) \
                       .order_by(attribute) 
            # Format count
            smry = {e[attribute]:e['count'] for e in smry}
            # Add data to response
            response.data['summary'] = smry
        # Return
        return response





