from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('list/food/', FoodListView.as_view(), name='food_list'),
    path('detail/food/<int:pk>/', FoodDetailView.as_view(), name='food_detail'),
    path('search/', FoodSearchView.as_view(), name ='searcher'),
]
