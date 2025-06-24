from django.contrib import admin
from .models import Staff,Orders,Parnters,Items,Category,Basket,Basketproducts,Cat,Case,Reels
@admin.register(Reels)
class Reels(admin.ModelAdmin):
    list_display = ['link']
@admin.register(Case)
class Case(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Cat)
class Cat(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Staff)
class Staff(admin.ModelAdmin):
    list_display = ['name','status']


@admin.register(Orders)
class Orders(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(Parnters)
class Parnters(admin.ModelAdmin):
    list_display = ['pictures']


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Items)
class Items(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(Basket)
class Basket(admin.ModelAdmin):
    list_display = ['name','phone']


@admin.register(Basketproducts)
class Basketproducts(admin.ModelAdmin):
    list_display = ['basket','items']