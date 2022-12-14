import os
import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from .fields import WEBPField


def image_folder(instance, filename):
    return 'photos/{}.webp'.format(uuid.uuid4().hex)


class PulsarProduct(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    vendor = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    status = models.TextField(choices=[
        ('В наличии', 'В наличии'),
        ('Под заказ', 'Под заказ'),
        ('Ожидается поступление', 'Ожидается поступление'),
        ('Нет в наличии', 'Нет в наличи'),
        ('Не производится', 'Не производится')])
    image = WEBPField(
        verbose_name=_('Image'),
        upload_to=image_folder,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

