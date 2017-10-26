# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Cactus(models.Model):

    user = models.ForeignKey(User)
    cactus_name = models.CharField(_('cactus name'), max_length=100)
    location = models.CharField(_('location'), max_length=100)
    flowers = models.CharField(_('flowers'), max_length=100)
    quantity = models.IntegerField(_('quantity'), default=0)
    image = models.ImageField(_('image'), upload_to='cactus_images', default='media/default.png')

    def __str__(self):
        return self.cactus_name

    class Meta:
        verbose_name = _('cactus')
        verbose_name_plural = _('cactuses')
