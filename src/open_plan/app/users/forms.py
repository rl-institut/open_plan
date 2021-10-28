from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    email = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "name@example.com",}
        ),
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'username')


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'username')

