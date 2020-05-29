import copy
import io
import json
import zipfile

import postcodes_io_api
from django.contrib.gis.geos import Point
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import formset_factory
from django.shortcuts import render

from dashboard.models import Patient, TestingCentre, DiagnosticTest
from .forms import dataUploadForm
from .models import CountryBorder, RegionBorder


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


def get_locations(lat, long):
    api = postcodes_io_api.Api(debug_http=False)
    resp = api.get_nearest_postcodes_for_coordinates(latitude=lat, longitude=long, limit=1, radius=2000)
    result = resp['result'] if ('result' in resp) and (resp['result'] != None) else []
    item = result[0] if len(result) > 0 else {}
    postcode = item['postcode'] if 'postcode' in item else str()
    pnt = Point(long, lat)

    # try and get region using local data, if that fails take data from postcodesAPI
    try:
        region = RegionBorder.objects.filter(mpoly__contains=pnt)[0].name
    except IndexError:
        region = item['region'] if 'region' in item else (item['country'] if 'country' in item else str())

    # try and take country from local data, if that fails and there is a region country is UK else unknown
    try:
        country = CountryBorder.objects.filter(mpoly__contains=pnt)[0].name
    except IndexError:
        if region:
            country = 'United Kingdom'
        else:
            country = ''

    return {"country": country, "region": region, "postcode": postcode}


def createModels(data):
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
