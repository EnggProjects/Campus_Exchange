from django.contrib import admin

from django.contrib import admin
from .models import Auction, Bid

# Register the Auction model
@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('product', 'start_time', 'end_time', 'starting_bid')
    search_fields = ('product__title',)  # Assuming Product has a 'title' field
    list_filter = ('start_time', 'end_time')

# Register the Bid model
@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('auction', 'bidder', 'amount', 'timestamp')
    search_fields = ('auction__product__title', 'bidder__username')  # Adjust field names as necessary
    list_filter = ('timestamp',)

