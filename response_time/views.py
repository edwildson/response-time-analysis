from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView

from .utils import analysis


# Create your views here.

def IndexView(request):
    base_template_name = 'base.html'

    if request.method == "POST":
        result = analysis(request.FILES['myfile'])
        
        	

    return render(request, 'index.html', {'base_template_name': base_template_name})


index = IndexView