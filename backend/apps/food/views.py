from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import TemplateView, ListView, DetailView


class IndexPage(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = 'products'


class FoodListView(ListView):
    model = Product
    template_name = 'food_list.html'
    context_object_name = 'products'

class FoodDetailView(DetailView):
    model = Product
    template_name = 'food_detail.html'
    context_object_name = 'product'

class FoodSearchView(ListView):
    model = Product
    template_name = 'food_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        search_text = self.request.GET.get('query')
        q = self.model.objects.filter(name__icontains=search_text)
        return q