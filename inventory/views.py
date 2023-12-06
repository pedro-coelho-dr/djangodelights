from decimal import Decimal
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Sum, F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm



class UserLoginView(LoginView):
    template_name = 'registration/login.html'

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/home.html'

class IngredientsListView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = 'inventory/ingredients_list.html'

class NewIngredientView(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'inventory/add_ingredient.html'
    success_url = reverse_lazy('ingredients_list')

class UpdateIngredientView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'inventory/update_ingredient.html'
    success_url = reverse_lazy('ingredients_list')

class MenuListView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = 'inventory/menu_list.html'

class NewMenuItemView(LoginRequiredMixin, CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'inventory/add_menu_item.html'
    success_url = reverse_lazy('menu_list')

class DeleteMenuItemView(LoginRequiredMixin, View):
    def get(self, request, menu_item_id):
        menu_item = MenuItem.objects.get(id=menu_item_id)
        menu_item.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

class NewRecipeRequirementView(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = 'inventory/add_recipe_requirement.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['menu_item'] = self.kwargs.get('menu_item_id')
        return initial

    def get_success_url(self):
        return reverse_lazy('menu_list')
    
class DeleteRecipeRequirementView(LoginRequiredMixin, View):
    def get(self, request, requirement_id):
        requirement = RecipeRequirement.objects.get(id=requirement_id)
        requirement.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
class PurchasesListView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = 'inventory/purchases_list.html'

class NewPurchaseView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/add_purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = MenuItem.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        menu_item_id = request.POST.get("menu_item")
        menu_item = MenuItem.objects.get(id=menu_item_id)

        can_make_item = all(
            requirement.ingredient.quantity >= requirement.quantity
            for requirement in menu_item.reciperequirement_set.all()
        )

        if can_make_item:
            for requirement in menu_item.reciperequirement_set.all():
                ingredient = requirement.ingredient
                ingredient.quantity -= requirement.quantity
                ingredient.save()
            Purchase.objects.create(menu_item=menu_item)
            return redirect('purchases_list')
        else:
            return render(request, self.template_name, {
                "error": "Not enough ingredients.",
                "menu_items": MenuItem.objects.all()
            })

class ReportView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/reports.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        purchases = Purchase.objects.all()
        context['total_revenue'] = purchases.aggregate(Sum('menu_item__price'))['menu_item__price__sum'] or Decimal('0.00')
        total_cost = Decimal('0.00')
        for purchase in purchases:
            total_cost += sum(
                Decimal(str(requirement.quantity)) * requirement.ingredient.unit_price
                for requirement in purchase.menu_item.reciperequirement_set.all()
            )
        context['total_cost'] = total_cost
        context['profit'] = context['total_revenue'] - total_cost
        return context
