from django.urls import path
from .views import *


urlpatterns = [
 path('order/entry/', UserEntryView.as_view(), name='order_entry')
]