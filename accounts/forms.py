from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser   # ✅ point to your custom user model
        fields = ("username", "email")  # you can add more like first_name, last_name

