from django.shortcuts import render, redirect
from django.views import View
from .models import Users
from .forms import UserForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = Users.objects.all()[:]
        return render(request, 'users/users.html', context={
            'users': users,
        })


class UserFormCreateView(SuccessMessageMixin, CreateView):

    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = _("The user has been successfully registered")
            return redirect('login')
        return render(request, 'users/create.html', {'form': form})


class UserFormUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = Users.objects.get(id=user_id)
        form = UserForm(instance=user)
        return render(request, 'users/update.html', {'form': form, 'user': user})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = Users.objects.get(id=user_id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users_list')
        return render(request, 'users/update.html', {'form': form, 'user': user})


class UserFormDeleteView(LoginRequiredMixin, DeleteView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = Users.objects.get(id=user_id)
        form = UserForm(instance=user)
        return render(request, 'users/delete.html', {'form': form, 'user': user})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = Users.objects.get(id=user_id)
        if user:
            user.delete()
        return redirect('users_list')
