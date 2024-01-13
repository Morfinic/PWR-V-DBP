from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path("item_list/", views.item_list, name="item_list"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/edit/", views.edit, name="edit"),
    path("new_item/", views.new_item, name="new_item"),
    path("new_wydawca/", views.new_wydawca, name="new_wydawca"),
    path("new_tematyka/", views.new_tematyka, name="new_tematyka"),
    path("<int:pk>/new_order/", views.new_order, name="new_order"),
    path("<int:pk>/item_list_category", views.item_list_category, name="item_list_category")
]
