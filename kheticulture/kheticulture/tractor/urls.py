from django.urls import path
from . import views

app_name = 'tractor'

urlpatterns = [
    path('', views.all_tractors, name='all_tractors'),
	path('add/', views.add, name='add'),
    
]
