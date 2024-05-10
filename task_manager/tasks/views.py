from .models import Task
from .forms import TaskForm
from .filters import TaskFilter
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django_filters.views import FilterView
from django.views.generic.detail import DetailView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class IndexView(FilterView):

    model = Task
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter


class TaskFormCreateView(SuccessMessageMixin, CreateView):

    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully created')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class TaskFormUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task changed successfully')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskFormDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task deleted successfully')

    def get(self, request, *args, **kwargs):
        if self.get_object().author != self.request.user:
            messages.error(request, _('Only the author of a task can delete it'))
            return redirect(reverse_lazy('tasks'))
        return super().get(request, *args, **kwargs)


class TaskReadView(DetailView):
    model = Task
    template_name = 'tasks/read.html'
    context_object_name = 'task'
