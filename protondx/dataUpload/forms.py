from django import forms
from dashboard.choices import GENDER, CENTRE_TYPE, DIAGNOSIS


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class dataUploadForm(forms.Form):

    first_name = forms.CharField(label='First name', max_length=50)
    last_name = forms.CharField(label='Last name', max_length=50)
    gender = forms.ChoiceField(label='Gender', choices=GENDER)
    dob = forms.DateField(label='Date of birth')
    patient_postcode = forms.CharField(label='Postcode', max_length=8)

    centre_type = forms.ChoiceField(label="Centre type", choices=CENTRE_TYPE)
    latitude = forms.FloatField(label="Latitude")
    longitude = forms.FloatField(label="Longitude")

    test_result = forms.ChoiceField(label="Result", choices=DIAGNOSIS)
    test_date = forms.DateTimeField(label="Date")
    comment = forms.Textarea()
