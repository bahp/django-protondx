"""
This module contains the views for the Dashboard App
"""
from django.shortcuts import render
from django.views.generic import TemplateView


# --------------
# VIEWS
# --------------

# Main dashboard / homepage
class DashView(TemplateView):
    """
    This view displays the dashboard
    """
    template_name = 'dashboard/dash.html'
