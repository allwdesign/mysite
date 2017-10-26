# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect, HttpResponse
from .models import Cactus
from .forms import CactusForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import ugettext as _


def index(request):
    """ To display all registered Cactuses """
    cactuses = Cactus.objects.all()
    form_cactus = CactusForm()
    return render(request, 'index.html', {'cactuses': cactuses,
                                            'form_cactus': form_cactus})


def detail(request, cactus_id):
    """ To display info about current Cactus """
    cactus = get_object_or_404(Cactus, id=cactus_id)
    return render(request, 'detail.html', {'cactus': cactus})


@login_required(login_url="/login/")
def post_cactus(request):
    """ To display form for adding a Cactus """
    form = CactusForm(request.POST, request.FILES)  # The view needs access to our uploaded files to save the image."""
    if form.is_valid():
        cactus = form.save(commit=False)
        cactus.user = request.user
        cactus.save()
        messages.success(request, _('Thank you! Your cactus added!'))
    return HttpResponseRedirect('/')  # Redirect to the homepage


def register(request):
    """ To display form for registration user """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            username = form.cleaned_data.get('username')
            passwd = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=passwd)
            login(request, user)
            messages.info(request, _('You have successfully registered!'))
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def profile(request):
    """ To display all the cacti user or a message asking user to add Cactus """
    user = request.user
    if user.is_authenticated():
        cactuses = Cactus.objects.filter(user=user)
        if len(cactuses) > 0:
            return render(request, 'profile.html', {'cactuses': cactuses})
        else:
            # If user is authenticated, but have not cactuses he will get a message and redirect homepage.
            messages.info(request, _('You have not yet registered cactuses. Add your cactus.'))
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def login_view(request):
    """ To display form for logging user """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
                else:
                    messages.warning(request, _('The account has been disabled!'))
            else:
                messages.warning(request, _('The username and password were incorrect.'))
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
