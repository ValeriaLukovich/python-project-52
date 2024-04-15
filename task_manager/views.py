from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from task_manager.article.forms import UserLoginForm
from django.views import View


class HomePageView(TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class UserLoginView(View):
    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('start_page')
        return render(request, 'login.html', {'form': form})
