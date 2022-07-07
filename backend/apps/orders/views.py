from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserEntryForm

class UserEntryView(TemplateView):
    template_name = 'order_entry.html'
    form_class = UserEntryForm
    success_url = 'index.html'