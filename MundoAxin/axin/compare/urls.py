from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"),name="login_user"),
    path('logout/', auth_views.LogoutView.as_view(next_page = "/"), name="index"),
    path('register/',views.register, name="register"),
    path('compare/', views.compare, name="compare"),
    path('wishlist/', views.wish_list, name="wish_list"),
    path('delete/<int:product_id>/', views.delete_wish, name="delete_wish"),

]