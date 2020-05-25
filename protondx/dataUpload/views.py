from django.views.generic.edit import FormView
from .forms import FileFieldForm


class dataUploadView(FormView):
    form_class = FileFieldForm
    template_name = 'dataUpload/dataUpload.html'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                print("file uploaded")
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
