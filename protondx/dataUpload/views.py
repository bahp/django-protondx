import copy
import io
import json
import zipfile

from django.contrib.gis.geos import Point
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import formset_factory
from django.shortcuts import render

from dashboard.models import Patient, TestingCentre, DiagnosticTest
from dashboard.fixtures.gen_location import get_locations
from .forms import dataUploadForm


# def appendZIP(data):
#     archive_orig = copy.deepcopy(data.get('raw_test_data'))
#     del data['raw_test_data']
#
#     updatedData = json.dumps(
#         data,
#         sort_keys=False,
#         indent=4,
#         cls=DjangoJSONEncoder
#     )
#
#     with zipfile.ZipFile(archive_orig, 'w') as zip_archive:
#         with zip_archive.open('updated/updated.json', 'w') as file1:
#             file1.write(b'compose-file-content...')
#
#     return archive_orig


def createModels(data):
    """
    Creates database entries for Patient, TestingCentre and DiagnosticTest using cleaned form data.

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
                    createModels(data)
        else:
            print(upload_formset.errors)
            # do something here
    else:
        upload_formset = UploadFormset(prefix='data', )
    return render(request, 'dataUpload/dataUpload.html', {
        'upload_formset': upload_formset,
    })
