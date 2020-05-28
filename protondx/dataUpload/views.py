from django.contrib.gis.geos import Point
from django.forms import formset_factory
from django.views.generic.edit import FormView

from dashboard.models import Patient, TestingCentre, DiagnosticTest
from .forms import FileFieldForm, dataUploadForm
from django.shortcuts import render
import postcodes_io_api


# class dataUploadView(FormView):
#     form_class = dataUploadForm
#     template_name = 'dataUpload/dataUpload.html'
#
#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         if form.is_valid():
#             for f in files:
#                 print("file uploaded")
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

def get_locations(lat, long):
    api = postcodes_io_api.Api(debug_http=False)
    resp = api.get_nearest_postcodes_for_coordinates(latitude=lat, longitude=long, limit=1)
    result = resp['result'] if ('result' in resp) and (resp['result'] != None) else []
    item = result[0] if len(result) > 0 else {}
    postcode = item['postcode'] if 'postcode' in item else str()
    country = "United Kingdom"
    region = item['region'] if 'region' in item else (item['country'] if 'country' in item else str())

    return {"country": country, "region": region, "postcode": postcode}


def createModels(data):
    patient = Patient.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        gender=data.get('gender'),
        dob=data.get('dob'),
        postcode=data.get('patient_postcode')
    )

    patient.save()

    location = get_locations(data['latitude'], data['longitude'])

    testing_centre = TestingCentre.objects.create(
        centre_type=data['centre_type'],
        coordinates=Point(data['longitude'], data['latitude']),
        country=location['country'],
        region=location['region'],
        postcode=location['postcode'],
    )

    testing_centre.save()

    diagnostic_test = DiagnosticTest.objects.create(
        testing_centre=testing_centre,
        patient=patient,
        test_result=data['test_result'],
        date_test=data['test_date'],
        comment=data.get('comment')
    )
    diagnostic_test.save()


def dataUploadView(request):

    UploadFormset = formset_factory(dataUploadForm)
    if request.method == 'POST':
        upload_formset = UploadFormset(request.POST, prefix='data')
        if upload_formset.is_valid():
            for f in upload_formset:
                data = f.cleaned_data
                if data:
                    createModels(data)
        else:
            print(upload_formset)
            # do something here
    else:
        upload_formset = UploadFormset(prefix='data',)
    return render(request, 'dataUpload/dataUpload.html', {
        'upload_formset': upload_formset,
    })
