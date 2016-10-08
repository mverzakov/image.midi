from django.shortcuts import HttpResponse
from django.views.generic.edit import FormView
from index.forms import IndexForm

# Create your views here.
#
# def index(request):
#     return HttpResponse("Play music")

class IndexView(FormView):
    template_name = 'index.html'
    form_class = IndexForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        file = form.cleaned_data['image']
        print file
        return self.form_invalid(form)
