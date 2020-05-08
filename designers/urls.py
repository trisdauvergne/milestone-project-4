from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_designers, name='all_designers'),
    path('designer-detail/', views.designer_detail, name='designer_detail'),
]
