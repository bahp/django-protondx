"""
This module is used to query the database for global or postcode level diagnostic and patient counts.
"""

from .models import Patient, DiagnosticTest


# --------------
# QUERIES
# --------------

def get_total_experiments():
    """
    Get the number of diagnostic tests stored in the database

    :return: Number of diagnostic tests
    :rtype: int
    """
    return DiagnosticTest.objects.count()


def get_negative_experiments():
    """
    Get the number of diagnostic tests stored in the database where the outcome is 'Negative'

    :return: Number of 'Negative' diagnostic tests
    :rtype: int
    """
    return DiagnosticTest.objects.filter(test_result=False).count()


def get_positive_experiments():
    """
    Get the number of diagnostic tests stored in the database where the outcome is 'Positive'

    :return: Number of 'Positive' diagnostic tests
    :rtype: int
    """
    return DiagnosticTest.objects.filter(test_result=True).count()


def get_individuals_tested():
    """
    Get the number of individual patients stored in the database

    :return: Number of patients
    :rtype: int
    """
    return Patient.objects.count()


def get_postcode_total_experiments(postcode):
    """
    Get the number of diagnostic tests made in a certain postcode

    :param string postcode: postcode
    :return: Number of diagnostic tests
    :rtype: int
    """
    return DiagnosticTest.objects.filter(testing_centre__postcode__startswith=postcode).count()


def get_postcode_negative_experiments(postcode):
    """
    Get the number of diagnostic tests where the outcome is 'Negative' for a certain postcode

    :param string postcode: postcode
    :return: Number of 'Negative' diagnostic tests
    :rtype: int:
    """
    return DiagnosticTest.objects.filter(testing_centre__postcode__startswith=postcode, test_result=False).count()


def get_postcode_positive_experiments(postcode):
    """
    Get the number of diagnostic tests where the outcome is 'Positive' for a certain postcode

    :param string postcode: postcode
    :return: Number of 'Positive' diagnostic tests
    :rtype: int:
    """
    return DiagnosticTest.objects.filter(testing_centre__postcode__startswith=postcode, test_result=True).count()


def get_postcode_individuals_tested(postcode):
    """
    Get the number of individual patients tested in a certain postcode

    :param string postcode: postcode
    :return: Number of patients
    :rtype: int
    """
    return DiagnosticTest \
        .objects \
        .select_related('patient') \
        .filter(testing_centre__postcode__startswith=postcode) \
        .values('patient_id') \
        .distinct() \
        .count()


def get_postcode_data(postcode):
    """
    Get testing data related to a postcode. Provides the total number of experiments,
    the number of positive and negative diagnostics and the number of patients tested.

    :param string postcode: postcode
    :return: Dictionary of query results
    :rtype: dict
    """
    data = {
        'total': get_postcode_total_experiments(postcode),
        'positive': get_postcode_positive_experiments(postcode),
        'negative': get_postcode_negative_experiments(postcode),
        'patients': get_postcode_individuals_tested(postcode),
    }

    return data
