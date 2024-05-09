from .models import Task
from .forms import TaskForm
from .filters import TaskFilter
from django.urls import reverse_lazy
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
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskFormUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task changed successfully')


class TaskFormDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task deleted successfully')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class TaskReadView(DetailView):
    model = Task
    template_name = 'tasks/read.html'
    context_object_name = 'task'
