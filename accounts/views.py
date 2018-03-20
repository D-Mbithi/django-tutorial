from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


# Create your views here.
def home(request):
    template = 'accounts/index.html'
    context = {}
    return render(request, template, context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/account/')
    else:
        form = RegistrationForm()
    context = {'form': form}
    template = 'accounts/signup.html'
    return render(request, template, context)


def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect("/account/profile/")
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {"form": form})
