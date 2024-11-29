# auctions/urls.py
from django.urls import path
from . import views
from .views import create_auction

urlpatterns = [
    path('active/', views.active_auctions, name='active_auctions'),  # Add this line
    path('<int:pk>/', views.auction_detail, name='auction_detail'),
    path('<int:auction_id>/bid/', views.place_bid, name='place_bid'),
    path('create/<int:product_id>/', create_auction, name='create_auction'),
]
