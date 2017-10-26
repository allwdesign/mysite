# -*- coding: utf-8 -*-
from django import forms
from .models import Cactus
from django.utils.translation import ugettext_lazy as _


class CactusForm(forms.ModelForm):
    class Meta:
        model = Cactus
        fields = ['cactus_name', 'location', 'flowers', 'quantity', 'image']


class LoginForm(forms.Form):
    username = forms.CharField(label=_('User Name'), max_length=64)
    password = forms.CharField(label=_('password'), widget=forms.PasswordInput())
