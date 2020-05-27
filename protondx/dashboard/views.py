from django.shortcuts import render
from django.views.generic import TemplateView

# Queries to count number of tests, cases, ...
from .queries import *


# --------------
# VIEWS
# --------------

# Main dashboard / homepage
class DashView(TemplateView):
    template_name = 'dashboard/dash.html'

    def get(self, request, **kwargs):
        context = {
            'count_total_exp': get_total_experiments(),
            'count_pos_exp': get_positive_experiments(),
            'count_neg_exp': get_negative_experiments(),
            'count_indiv_patients': get_individuals_tested(),
        }
        return render(request, self.template_name, context)

