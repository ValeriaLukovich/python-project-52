from django.contrib.auth.forms import (UserCreationForm)
from .models import Users


class UserForm(UserCreationForm):

    class Meta:
        model = Users
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        )


class UpdateUserForm(UserForm):

    def clean_username(self):
        username = self.cleaned_data['username']
        if Users.objects.filter(username=username).exists():
            username = self.cleaned_data['username']
        return username
