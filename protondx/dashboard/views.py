from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Patient, TestingCentre, DiagnosticTest
from .forms import PostcodeForm
from .queries import *


# --------------
# VIEWS
# --------------

class DashView(TemplateView):
    template_name = 'dashboard/dash.html'

    # #####
    # remove test entries from context
    # #####
    def get(self, request, **kwargs):
        form = PostcodeForm()
        context = {
            'count_total_exp': get_total_experiments(),
            'count_pos_exp': get_positive_experiments(),
            'count_neg_exp': get_negative_experiments(),
            'count_indiv_patients': get_individuals_tested(),
            'test1': get_postcode_data('SW5 0TU'),
            'test2': get_postcode_data('SW1A 1AA'),
            'form': form,
        }
        return render(request, self.template_name, context)

    # Not currently used (Might be useful when querying postcode info)
    def post(self, request):
        form = PostcodeForm(request.POST)
        if form.is_valid():
            post_code_query = get_postcode_data(form.cleaned_data['post'])
            form = PostcodeForm()
            context = {
                'count_total_exp': get_total_experiments(),
                'count_pos_exp': get_positive_experiments(),
                'count_neg_exp': get_negative_experiments(),
                'count_indiv_patients': get_individuals_tested(),
                'test1': get_postcode_data('SW5 0TU'),
                'test2': get_postcode_data('SW1A 1AA'),
                'form': form,
                'post_code_query': post_code_query
            }
            return render(request, self.template_name, context)
