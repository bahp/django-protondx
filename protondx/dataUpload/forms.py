from django import forms
from dashboard.choices import GENDER, CENTRE_TYPE, DIAGNOSIS


# override colon at end of form labels
class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(BaseForm, self).__init__(*args, **kwargs)


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class dataUploadForm(BaseForm):
    first_name = forms.CharField(label='First name', max_length=50, widget=forms.TextInput(attrs={'required': True}))
    last_name = forms.CharField(label='Last name', max_length=50,  widget=forms.TextInput(attrs={'required': True}))
    gender = forms.ChoiceField(label='Gender', choices=GENDER, required=False)
    dob = forms.DateField(label='Date of birth', required=False)
    patient_postcode = forms.CharField(label='Postcode', max_length=8, required=False)

    centre_type = forms.ChoiceField(label="Centre type", choices=CENTRE_TYPE)
    latitude = forms.FloatField(label="Latitude",  widget=forms.TextInput(attrs={'required': True}))
    longitude = forms.FloatField(label="Longitude",  widget=forms.TextInput(attrs={'required': True}))

    test_result = forms.ChoiceField(label="Result", choices=DIAGNOSIS,)
    test_date = forms.DateTimeField(label="Date",  widget=forms.TextInput(attrs={'required': True}))
    raw_test_data = forms.FileField(label=False)
    comment = forms.CharField(widget=forms.Textarea, required=False)
