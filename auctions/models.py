from django.db import models

# Create your models here.
# auctions/models.py
from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()


class Auction(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Auction for {self.product.title}"

class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

