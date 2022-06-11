from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, CreateView

from .utils import analysis


# Create your views here.

def IndexView(request):
    base_template_name = 'base.html'

    def get_context_data(self, *args, **kwargs):
        # texts = ['Lorem ipsum', 'dolor sit amet', 'consectetur']
        context = {
        }
        return context

    if request.method == "POST":
        result = analysis(request.FILES['myfile'])
        
        return render(request, 'index.html', {'context': result, 'base_template_name': base_template_name})
        
        	

    return render(request, 'index.html', {'base_template_name': base_template_name})




index = IndexView
