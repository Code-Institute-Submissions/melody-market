from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='items'),
    path('<product_id>', views.item_details, name='item_details'),
    path('', views.item_condition, name='item_condition'),
    path('', views.item_sale, name='item_sale'),
]
