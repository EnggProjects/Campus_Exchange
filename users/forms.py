from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, College
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    college = forms.ModelChoiceField(
        queryset=College.objects.all(),
        empty_label="Select a college",
        required=True
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'college', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'bio', 'location', 'birth_date']

    def clean_username(self):
        username = self.cleaned_data['username']
        if get_user_model().objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise ValidationError("A user with that username already exists.")
        return username