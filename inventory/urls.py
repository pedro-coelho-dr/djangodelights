from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(next_page='home'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.HomeView.as_view(), name='home'),
    path('ingredients/', views.IngredientsListView.as_view(), name='ingredients_list'),
    path('ingredients/new/', views.NewIngredientView.as_view(), name='add_ingredient'),
    path('ingredients/<int:pk>/update/', views.UpdateIngredientView.as_view(), name='update_ingredient'),
    path('menu/', views.MenuListView.as_view(), name='menu_list'),
    path('menu/new/', views.NewMenuItemView.as_view(), name='add_menu_item'),
    path('reciperequirement/new/<int:menu_item_id>/', views.NewRecipeRequirementView.as_view(), name='add_recipe_requirement'),
    path('purchases/', views.PurchasesListView.as_view(), name='purchases_list'),
    path('purchases/new/', views.NewPurchaseView.as_view(), name='add_purchase'),
    path('reports/', views.ReportView.as_view(), name='reports'),
    path('reciperequirement/delete/<int:requirement_id>/', views.DeleteRecipeRequirementView.as_view(), name='delete_recipe_requirement'),
    path('menu/delete/<int:menu_item_id>/', views.DeleteMenuItemView.as_view(), name='delete_menu_item'),
]
