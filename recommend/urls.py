from django.urls import path
from . import views

urlpatterns = [
    #path('', views.recommend_view, name='recommend_view'),
    path('', views.index, name='profile_list'),
]
