from django.contrib import admin
from .models import Staff,Orders,Parnters,Items,Category

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