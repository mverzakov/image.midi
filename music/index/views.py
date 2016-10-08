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

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(IndexView, self).form_valid(form)
