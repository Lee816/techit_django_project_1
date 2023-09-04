from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login

from .forms import RegisterUserForm

# Create your views here.

class RegisterUserView(generic.CreateView):
    template_name = 'accounts/registrations.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('accountsregister')
    
    def form_valid(self,form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(usernae=cd['username'],password=cd['password'])
        login(self.request, user)
        return result