# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CactusAppConfig(AppConfig):
    name = 'cactus_app'
    verbose_name = _('Cactus App')
