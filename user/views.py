from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, reverse
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_protect

from .forms import SignupForm, SigninForm
from .models import User


class ProfileView(generic.ListView):
    model = User
    template_name = 'user/profile.html'


@csrf_protect
def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('event:index'))
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.signin(request)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('event:index'))
        else:
            return render(request, 'user/signup.html', {'form': form, 'error': True})
    else:
        form = SignupForm()
    return render(request, 'user/signup.html', {'form': form})


@csrf_protect
def signin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('event:index'))
    if request.method == 'POST':
        form = SigninForm(data=request.POST)
        if form.is_valid():
            user = form.signin(request)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('event:index'))
        else:
            return render(request, 'user/signin.html', {'form': form, 'error': True})
    else:
        form = SigninForm()
    return render(request, 'user/signin.html', {'form': form})


@csrf_protect
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('event:index'))
