from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_prints, name='all_prints'),
    path('add-print/', views.add_print, name='add_print'),
]
