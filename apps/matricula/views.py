from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Inicio(TemplateView):
    template_name = 'matricula/index.html'