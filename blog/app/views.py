from django.shortcuts import render
from django.views import generic
from .models import Table
# Create your views here.


class home(generic.DetailView):
    model=Table
    template_name = 'home.html'
    
class about(generic.TemplateView):
    template_name ='about.html'

class index(generic.ListView):
    queryset      = Table.objects.all()
    template_name = 'index.html'