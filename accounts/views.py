#from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


class LoginView(FormView):
    success_url = reverse_lazy('127.0.0.1:8000')
