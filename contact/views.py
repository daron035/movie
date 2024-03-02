from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .service import send
from .tasks import send_spam_email

class Contact(CreateView):
    form_class = ContactForm
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.save()
        # send(form.instance.email)
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)