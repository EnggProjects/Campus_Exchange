# auctions/views.py
from django.shortcuts import render, redirect,  get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Auction, Bid
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import AuctionForm 

def active_auctions(request):
    current_time = timezone.now()
    auctions = Auction.objects.filter(end_time__gt=current_time)  # Fetch ongoing auctions
    return render(request, 'auctions/active_auctions.html', {'auctions': auctions})



# auctions/views.py
def auction_detail(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    bids = auction.bid_set.all()  # Get all bids for the auction
    highest_bid = bids.order_by('-amount').first()  # Get the highest bid

    return render(request, 'auctions/auction_detail.html', {
        'auction': auction,
        'highest_bid': highest_bid,
        'bids': bids,
    })


# Your existing place_bid function
def place_bid(request, auction_id):
    if request.method == 'POST':
        auction = Auction.objects.get(id=auction_id)
        amount = request.POST.get('amount')
        Bid.objects.create(auction=auction, bidder=request.user, amount=amount)
        return redirect('auction_detail', pk=auction_id)



from datetime import timedelta

@login_required
def create_auction(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Check if the product is already in an auction
    if Auction.objects.filter(product=product).exists():
        return HttpResponse("This product is already in an auction.")
    
    if request.method == 'POST':
        form = AuctionForm(request.POST)
        if form.is_valid():
            auction = form.save(commit=False)
            auction.product = product
            auction.start_time = timezone.now()
            auction.end_time = timezone.now() + timedelta(hours=48)  # Set end time to 48 hours from now
            auction.save()
            return redirect('auction_detail', pk=auction.id)  # Use pk instead of auction_id for clarity
    else:
        form = AuctionForm()

    return render(request, 'auctions/create_auction.html', {'form': form, 'product': product})
