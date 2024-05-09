from django.shortcuts import render
from django.views import View
from .models import Label
from .forms import LabelForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(View):

    def get(self, request, *args, **kwargs):
        labels = Label.objects.all()[:]
        return render(request, 'labels/labels.html', context={
            'labels': labels,
        })


class LabelFormCreateView(SuccessMessageMixin, CreateView):

    form_class = LabelForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels')
    success_message = _('Tag successfully created')


class LabelFormUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Label
    form_class = LabelForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels')
    success_message = _('Tag changed successfully')


class LabelFormDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels')
    success_message = _('Tag successfully deleted')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
