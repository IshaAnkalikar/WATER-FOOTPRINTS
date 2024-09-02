from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('results/', views.results, name='results'),
    path('awareness/', views.awareness, name='awareness'),  # Add this line
]
