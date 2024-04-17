from django.urls import path
from . import views

app_name =  'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('category-list/', views.list_category, name='category-list'),
    path('category-create/', views.create_category, name='category-create'),
    path('category-detail/<int:id>/', views.detail_category, name='category-detail'),
    path('category-edit/<int:id>/', views.edit_category, name='category-edit'),
    path('category-delete/<int:id>/', views.delete_category, name='category-delete'),
    
    
    path('register/', views.register, name='register'),
    path('log-in/', views.log_in, name='log_in'),
    path('log-out/', views.log_out, name='log_out'),

    path('region-list/', views.list_region, name='region-list'),
    path('region-create/', views.create_region, name='region-create'),
    path('region-detail/<int:id>/', views.detail_region, name='region-detail'),
    path('region-edit/<int:id>/', views.edit_region, name='region-edit'),
    path('region-delete/<int:id>/', views.delete_region, name='region-delete'),

    path('post-detail/<int:id>/', views.detail_post, name='post-detail'),
    path('post-create/', views.create_post, name='post-create'),
    path('post-edit/<int:id>/', views.edit_post, name='post-edit'),
    path('post-delete/<int:id>/', views.delete_post, name='post-delete'),
    path('post-list/', views.list_post, name='post-list'),
]