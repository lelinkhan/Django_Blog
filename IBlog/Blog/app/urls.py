from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post_detail/<slug:url>/', views.post, name='post_detail'),
    path('post_category/<slug:url>/', views.category, name='post_category'),
    path('search/', views.search, name='search'),

]