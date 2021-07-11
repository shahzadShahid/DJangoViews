from django.urls import path
from products.views import product_list_view,dynamic_lookup_view,product_delete_view,product_create_view


app_name = 'products'
urlpatterns = [
    path('',product_list_view),
    path('create/',product_create_view),
    path('<int:id>/detail/',dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete/',product_delete_view, name='product')

]
