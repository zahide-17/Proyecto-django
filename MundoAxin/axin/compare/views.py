from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import CustomUserCreationForm
from .models import Product,User,Product_Store,Wish_list,Store,Category

from .serializers import UserSerializer,StoreSerializer,CategorySerializer,ProductStoreSerializer,ProductSerializer,WishListSerializer
from rest_framework import viewsets

# Create your views here.
def index(request):
    """ Vista para atender la petición de la url / """
    # Obteniendo los datos mediantes consultas
    product = Product.objects.all()
    return render(request, "products/index.html", {"product":product})

@login_required
def compare(request):
    product = Product.objects.all()
    product_Store = Product_Store.objects.all()
    return render(request, "products/compare.html", {"product":product, "product_Store":product_Store})

@login_required
def wish_list(request):
    wish_product = Wish_list.objects.all()
    product_Store = Product_Store.objects.all()
    return render(request, "products/wishList.html", {"wish_product":wish_product, "product_Store":product_Store})

@login_required()
def delete_wish(request, product_id):
    """ Atiende la petición GET /wishList/eliminar/<int:idProduct>/ """
    print("aqui", id_product)
    # Se obtienen los objetos correspondientes a los id's
    wish_product = Wish_list.objects.get(fk= product_id)
    # Se elimina el tour
    wish_product.delete()
    return redirect("/wishlist/")


#***********************************************************
def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html")
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            
            user = User.form.save()
            login(request, user)
            return reder(request, "/", {})

# Vistas basadas en clases para Django Rest
class UserViewSet(viewsets.ModelViewSet):
   """API que permite realizar operaciones en la tabla User"""
   # Se define el conjunto de datos sobre el que va a operar la vista,
   # en este caso sobre todos los users disponibles.
   queryset = User.objects.all().order_by('name')
   # Se define el Serializador encargado de transformar la peticiones
   # en formato JSON a objetos de Django y de Django a JSON.
   serializer_class = UserSerializer

class StoreViewSet(viewsets.ModelViewSet):
   """API que permite realizar operaciones en la tabla Store"""
   queryset = Store.objects.all().order_by('id_store')
   serializer_class = StoreSerializer

class CategoryViewSet(viewsets.ModelViewSet):
   """API que permite realizar operaciones en la tabla User"""
   queryset = Category.objects.all().order_by('name')
   serializer_class = CategorySerializer

class ProductStoreViewSet(viewsets.ModelViewSet):
   """API que permite realizar operaciones en la tabla Product_Store"""
   queryset = Product_Store.objects.all().order_by('id_product')
   serializer_class = ProductStoreSerializer

class ProductViewSet(viewsets.ModelViewSet):
   """API que permite realizar operaciones en la tabla Product"""
   queryset = Product.objects.all().order_by('name_product')
   serializer_class = ProductSerializer

class WishListViewSet(viewsets.ModelViewSet):
   """API que permite realizar operaciones en la tabla Wish_list"""
   queryset = Wish_list.objects.all().order_by('email_list')
   serializer_class = WishListSerializer

""" def login_user(request):
    ""Atiende las peticiones de GET /login/""
    # Si hay datos vía POST se procesan
    next = request.GET.get("next","/")
    if request.method == "POST":
         # Se obtienen los datos del formulario
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)   
        
        if user is not None:
            # Se agregan datos al request para mantener activa la sesión
            login(request, user)
            # Y redireccionamos a next
            return redirect(next)
        else:
            # Usuario malo
            msg = "Datos incorrectos, intente de nuevo!"
    else:
        # Si no hay datos POST
        msg = "Request invalido"
    return render(request, "registration/login.html")

def logout_user(request):
    ""Atiende las peticiones de GET /logout/ ""
    # Se cierra la sesión del usuario actual
    logout(request)
    return redirect("/") """