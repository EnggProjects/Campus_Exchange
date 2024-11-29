from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    CATEGORIES = (
        ('books', 'Books'),
        ('electronics', 'Electronics'),
        ('furniture', 'Furniture'),
        ('other', 'Other'),
    )
    
    seller = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user who is selling the product
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    condition = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    # New field to link the product to the seller's college
    college = models.ForeignKey('users.College', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
