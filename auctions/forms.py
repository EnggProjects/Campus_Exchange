# auctions/forms.py
from django import forms
from .models import Auction

class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['starting_bid']  # Include fields you want the user to fill out

