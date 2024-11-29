# products/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'condition', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Product Description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'condition': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Condition'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
