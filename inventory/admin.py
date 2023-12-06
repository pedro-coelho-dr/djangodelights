from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit', 'unit_price')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title',)

@admin.register(RecipeRequirement)
class RecipeRequirementAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'ingredient', 'quantity')

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'timestamp')
    list_filter = ('timestamp',)