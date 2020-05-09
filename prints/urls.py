from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_prints, name='all_prints'),
    path('add-print/', views.add_print, name='add_print'),
    path('single-print/<print_id>/', views.single_print, name='single_print'),
    path('delete-print/<print_id>/', views.delete_print, name='delete_print'),
]
