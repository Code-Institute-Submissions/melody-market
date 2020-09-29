from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='items'),
    path('', views.item_condition, name='item_condition'),
    path('sale/', views.item_sale, name='item_sale'),
    path('<int:product_id>/', views.item_details, name='item_details'),
    path('add/', views.add_item, name='add_item'),
    path('edit/<int:product_id>/', views.edit_item, name='edit_item'),
    path('delete/<int:product_id>/', views.delete_item, name='delete_item'),
]
