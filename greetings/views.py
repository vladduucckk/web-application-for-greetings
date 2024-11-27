from django.core.mail import send_mail
from django.shortcuts import render, redirect

from deployDjango import settings
from .models import Researcher
from .forms import GreetingForm, EmailForm


def greetings_home(request):
    data = Researcher.objects.order_by('-joined_in')
    return render(request, 'home.html', context={'data': data})


def add_greeting(request):
    if request.method == 'POST':
        form = GreetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('greetings-home')
        else:
            errors = form.errors
            form = GreetingForm()
            return render(request, 'add.html', context={'form': form, 'errors': errors})
    else:
        form = GreetingForm()
        return render(request, 'add.html', context={'form': form})


def greeting_email(request):
    subject = "Greetings"
    message = "Please, don’t ask me to greet you anymore, I’m already tired."
    from_email = settings.EMAIL_HOST_USER
    alert = "Check your email, you’ve been sent a greeting"
    form = EmailForm(request.GET)
    if form.is_valid():
        email = form.cleaned_data['email']
        send_mail(subject, message, from_email, [email])
        return render(request, 'email.html', context={'form': form, 'alert': alert})
    else:
        return render(request, 'email.html', context={'form': form})
