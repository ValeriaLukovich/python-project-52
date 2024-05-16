from .models import Label
from .forms import LabelForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import ProtectedError
from django.views.generic.list import ListView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(ListView):

    model = Label
    template_name = 'labels/labels.html'
    context_object_name = 'labels'


class LabelFormCreateView(SuccessMessageMixin, CreateView):

    form_class = LabelForm
    template_name = 'create.html'
    success_url = reverse_lazy('labels')
    success_message = _('Tag successfully created')
    extra_context = {'title': _('Create tag'),
                     'target': 'label_create',
                     'action': _('Create')}


class LabelFormUpdateView(LoginRequiredMixin,
                          SuccessMessageMixin,
                          UpdateView):

    model = Label
    form_class = LabelForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels')
    success_message = _('Tag changed successfully')


class LabelFormDeleteView(LoginRequiredMixin,
                          SuccessMessageMixin,
                          DeleteView):
    model = Label
    template_name = 'delete.html'
    success_url = reverse_lazy('labels')
    success_message = _('Tag successfully deleted')
    extra_context = {'action': _('Delete tag')}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object().name
        return context

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.warning(request, _("Cannot delete label because it is in use"))
            return redirect(reverse_lazy('labels'))
