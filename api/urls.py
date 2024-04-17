from . import views
from django.urls import path

urlpatterns = [
    # ----------- category api -------------
    path('category/list/', views.category_list),
    path('category/detail/<int:id>/', views.category_detail),
    
    # ------------post api -----------------
    path('post/detail/<int:id>/', views.post_detail),
    path('post/list', views.post_list),
]
