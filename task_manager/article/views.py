from .models import Users
from .forms import UserForm, UpdateUserForm
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = Users.objects.all()[:]
        return render(request, 'users/users.html', context={
            'users': users,
        })


class UserFormCreateView(SuccessMessageMixin, CreateView):

    model = Users
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _("The user has been successfully registered")


class UserFormUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Users
    form_class = UpdateUserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users_list')
    success_message = _("The user has been successfully edited")
    raise_exception = True

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _("You are not logged in! Please log in."))
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if self.get_object() != self.request.user:
            messages.error(request, _("You do not have the rights to change another user."))
            return redirect(reverse_lazy('users_list'))
        return super().get(request, *args, **kwargs)


class UserFormDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):

    model = Users
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users_list')
    success_message = _("The user has been successfully deleted")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _("You are not logged in! Please log in."))
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if self.get_object() != self.request.user:
            messages.error(request, _("You do not have the rights to delete another user."))
            return redirect(reverse_lazy('users_list'))
        return super().get(request, *args, **kwargs)
