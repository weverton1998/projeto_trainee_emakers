from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.conf import settings

from .forms import Create_User, User_Password_Reset_Form

class SignUp(generic.CreateView):
    form_class = Create_User
    sucess_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class Reset_Password_View(PasswordResetView):
    def get(self, request, *args, **kwargs):
        return redirect('/')
    
    email_template_name = 'emails/passwordreset.txt'
    from_email = settings.EMAIL_HOST_USER
    html_template_name = 'emails/passwordreset.html'
    form_class = User_Password_Reset_Form