from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, reverse
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import SignupForm, SigninForm, UpdateForm
from .models import User


class ProfileView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'user/pages/profile.html'
    redirect_field_name = 'redirect'


def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user:profile') + '#events')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.signin()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('user:profile') + '#events')
    else:
        form = SignupForm()
    return render(request, 'user/pages/signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user:profile') + '#events')
    if request.method == 'POST':
        form = SigninForm(data=request.POST)
        if form.is_valid():
            user = form.signin()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('user:profile') + '#events')
    else:
        form = SigninForm()
    return render(request, 'user/pages/signin.html', {'form': form})


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('event:index'))


@login_required(redirect_field_name='redirect')
def update(request):
    if request.method == 'POST':
        form = UpdateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile') + '#events')
    else:
        form = UpdateForm(instance=request.user)
    return render(request, 'user/pages/profile.html', {'form': form})
