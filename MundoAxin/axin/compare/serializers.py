from rest_framework import serializers
from .models import User, Store, Category, Product_Store, Product, Wish_list

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para User """
    class Meta:
        # Se define sobre que modelo actua
        model = User
        # Se definen los campos a incluir
        fields = ('alias','name', 'last_name', 'email', 'birth_date', 'gender', 'city')

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para User """
    class Meta:
        # Se define sobre que modelo actua
        model = Store
        # Se definen los campos a incluir
        fields = ('id_store','name', 'url', 'number_products')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para User """
    class Meta:
        # Se define sobre que modelo actua
        model = Category
        # Se definen los campos a incluir
        fields = ('name',)

class ProductStoreSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para User """
    class Meta:
        # Se define sobre que modelo actua
        model = Product_Store
        # Se definen los campos a incluir
        fields = ('id_product','name_product','mark','price','description','image','id_store','name_category')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para User """
    class Meta:
        # Se define sobre que modelo actua
        model = Product
        # Se definen los campos a incluir
        fields = ('name_product','mark','image','name_category','product_store')

class WishListSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para User """
    class Meta:
        # Se define sobre que modelo actua
        model = Wish_list
        # Se definen los campos a incluir
        fields = ('email_list','id_product')


