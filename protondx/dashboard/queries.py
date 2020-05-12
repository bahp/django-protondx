from .models import Patient, DiagnosticTest


# --------------
# QUERIES
# --------------

def get_total_experiments():
    return DiagnosticTest.objects.count()


def get_negative_experiments():
    return DiagnosticTest.objects.filter(test_result=False).count()


def get_positive_experiments():
    return DiagnosticTest.objects.filter(test_result=True).count()


def get_individuals_tested():
    return Patient.objects.count()


def get_postcode_total_experiments(postcode):
    return DiagnosticTest.objects.filter(postcode__startswith=postcode).count()


def get_postcode_negative_experiments(postcode):
    return DiagnosticTest.objects.filter(postcode__startswith=postcode, test_result=False).count()


def get_postcode_positive_experiments(postcode):
    return DiagnosticTest.objects.filter(postcode__startswith=postcode, test_result=True).count()


def get_postcode_individuals_tested(postcode):
    return DiagnosticTest \
        .objects \
        .select_related('patient') \
        .filter(postcode__startswith=postcode) \
        .values('patient_id') \
        .distinct() \
        .count()


def get_postcode_data(postcode):
    data = {
        'total': get_postcode_total_experiments(postcode),
        'positive': get_postcode_positive_experiments(postcode),
        'negative': get_postcode_negative_experiments(postcode),
        'patients': get_postcode_individuals_tested(postcode),
    }

    return data
