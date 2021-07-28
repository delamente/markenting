from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, ListView

from .models import Contact, Service


def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})


class ServiceListView(ListView):
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'services'


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_detail.html'
    context_object_name = 'service'


class ContactView(SuccessMessageMixin, CreateView):
    model = Contact
    fields = ('name', 'email_or_phone', 'message')
    template_name = 'contact.html'
    success_message = '¡Mensaje enviado! Te responderemos en breve'
    success_url = reverse_lazy('contact')
