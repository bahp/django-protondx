from django.forms import inlineformset_factory
from django.views.generic.edit import FormView
from .forms import FileFieldForm, dataUploadForm

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


from django.forms import formset_factory
from django.shortcuts import render


def dataUploadView(request):
    UploadFormset = formset_factory(dataUploadForm)
    if request.method == 'POST':
        upload_formset = UploadFormset(request.POST, prefix='data')
        if upload_formset.is_valid():
            for f in upload_formset:
                data = f.cleaned_data
                print(data)
        else:
            print("not valid")

            # save models here
    else:
        upload_formset = UploadFormset(prefix='data')
    return render(request, 'dataUpload/dataUpload.html', {
        'upload_formset': upload_formset,
    })
