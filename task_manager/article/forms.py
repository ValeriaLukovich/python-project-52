from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordChangeForm
)
from django.utils.translation import gettext_lazy as _
from .models import Users


class UserForm(UserCreationForm):
    first_name = forms.CharField(label=_('First name'), widget=forms.TextInput)
    last_name = forms.CharField(label=_('Last name'), widget=forms.TextInput)
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput,
        help_text=_("Obligatory field. No more than 150 characters. Only letters, numbers and symbols @/./+/-/_."),
    )
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput,
        help_text=_("Your password must contain at least 3 characters.")
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput,
        help_text=_("To confirm, please enter your password again.")
    )
    class Meta:
        model = Users
        fields = (
            'first_name',
            'last_login',
            'last_name',
            'username',
            'password1',
            'password2',
        )

        
class UserLoginForm(AuthenticationForm, PasswordChangeForm):
    username = forms.CharField(label=_('Username'), widget=forms.TextInput)
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['username', 'password']
