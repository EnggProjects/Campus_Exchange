from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.product_list, name='product_list'),  # All products
    path('create/', views.create_product, name='create_product'),  # Create a new product
    path('my-products/', views.my_products, name='my_products'),  # User's products
    path('<int:pk>/', views.product_detail, name='product_detail'),  # Product detail
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
