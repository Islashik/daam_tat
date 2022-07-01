from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import TemplateView, ListView


class IndexPage(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = 'products'