"""axin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from compare import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'stores',views.StoreViewSet)
router.register(r'categorys',views.CategoryViewSet)
router.register(r'productstore',views.ProductStoreViewSet)
router.register(r'products',views.ProductViewSet)
router.register(r'wishlists',views.WishListViewSet)
                                  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('compare.urls')),

    # Rutas para la url /api/
    path("api/",include(router.urls)),
    # Rutas para la autenticación url /api/auth/
    path("api/auth/",include("rest_framework.urls", namespace="rest_framework")),
]
