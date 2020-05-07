from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_designers, name='all_designers'),
    path('all-designers-temp', views.all_designers_temp, name='all_designers_temp'),
]
