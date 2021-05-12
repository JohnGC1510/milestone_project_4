from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_home, name="store"),
    path('<product_id>', views.product_detail, name="product_detail")
]
