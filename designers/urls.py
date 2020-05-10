from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_designers, name='all_designers'),
    path('designer-detail/<designer_id>/', views.designer_detail, name='designer_detail'),
    path('designer-profile/<designer_id>', views.designer_profile, name='designer_profile'),
    path('create-designer-profile/<user_id>/', views.create_designer_profile, name='create_designer_profile'),
    path('edit-designer-profile/', views.edit_designer_profile, name='edit_designer_profile'),
]
