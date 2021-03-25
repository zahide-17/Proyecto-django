from django.contrib import admin
from .models import User, Store, Category, Product_Store,Product, Wish_list

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("alias", "email","password", "birth_date")

class StoreAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id_store", "name","number_products", "url")

class CategoryAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("name",)

class ProductStoreAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id_product","name_product","mark","price","name_category")

class ProductAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("name_product","mark","id_product","name_category")

class WishListAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("email_list","id_product")

admin.site.register(User, UserAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product_Store, ProductStoreAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Wish_list, WishListAdmin)
