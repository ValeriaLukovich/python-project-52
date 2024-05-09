from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from task_manager.article.forms import UserLoginForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin


class HomePageView(TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'
    success_message = _("You are logged in")


class UserLogoutView(SuccessMessageMixin, LogoutView):

    next_page = reverse_lazy('start_page')
