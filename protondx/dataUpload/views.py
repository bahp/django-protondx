from django.contrib.gis.geos import Point
from django.forms import formset_factory
from django.shortcuts import render

from dashboard.models import Patient, TestingCentre, DiagnosticTest
from dashboard.fixtures.gen_location import get_locations
from .forms import dataUploadForm

# Login required
from django.contrib.auth.decorators import login_required

# Store user who added model
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_text


def createModels(request, data):
    """
    Creates database entries for Patient, TestingCentre and DiagnosticTest using cleaned form data.

    :param request: POST request. Contains user information
    :param dict data: Cleaned Diagnostic Data
    :return:
    """
    patient = Patient.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        gender=data.get('gender'),
        dob=data.get('dob'),
        postcode=data.get('patient_postcode')
    )

    location = get_locations(data['latitude'], data['longitude'])

    testing_centre = TestingCentre.objects.create(
        centre_type=data['centre_type'],
        coordinates=Point(data['longitude'], data['latitude']),
        country=location['country'],
        region=location['region'],
        postcode=location['postcode'],
        county=location['county'],
    )

    diagnostic_test = DiagnosticTest.objects.create(
        testing_centre=testing_centre,
        patient=patient,
        test_result=data['test_result'],
        date_test=data['test_date'],
        comment=data.get('comment'),
        raw_test_data=data.get('raw_test_data')
    )

    patient.save()
    testing_centre.save()
    diagnostic_test.save()

    LogEntry.objects.log_action(
        user_id=request.user.pk,
        content_type_id=ContentType.objects.get_for_model(patient).pk,
        object_id=patient.pk,
        object_repr=force_text(patient),
        action_flag=ADDITION,
        change_message='ADDED'
    )

    LogEntry.objects.log_action(
        user_id=request.user.pk,
        content_type_id=ContentType.objects.get_for_model(testing_centre).pk,
        object_id=testing_centre.pk,
        object_repr=force_text(testing_centre),
        action_flag=ADDITION,
        change_message='ADDED'
    )

    LogEntry.objects.log_action(
        user_id=request.user.pk,
        content_type_id=ContentType.objects.get_for_model(diagnostic_test).pk,
        object_id=diagnostic_test.pk,
        object_repr=force_text(diagnostic_test),
        action_flag=ADDITION,
        change_message='ADDED'
    )


@login_required
def dataUploadView(request):
    """
    This view displays the dataUpload page. Deals with POST and GET methods to supply forms and
    receive the completed forms.

    :param request: Request
    :return:

    ..todo: Deal with exceptions relating to missing form entries, or otherwise invalid data.
    """
    UploadFormset = formset_factory(dataUploadForm)
    if request.method == 'POST':
        upload_formset = UploadFormset(request.POST, request.FILES, prefix='data')
        if upload_formset.is_valid():
            for f in upload_formset:
                data = f.cleaned_data
                if data:
                    createModels(request, data)
        else:
            print(upload_formset.errors)
            # do something here
    else:
        upload_formset = UploadFormset(prefix='data', )
    return render(request, 'dataUpload/dataUpload.html', {
        'upload_formset': upload_formset,
    })
