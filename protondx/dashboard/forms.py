from django import forms


# Not currently used (Might be useful when querying postcode info)

class PostcodeForm(forms.Form):
    post = forms.CharField()
