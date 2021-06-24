from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_home, name="store"),
    path('<int:product_id>/', views.product_detail, name="product_detail"),
    path('add_product/', views.add_product, name="add_product"),
]
