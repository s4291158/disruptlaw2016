from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseUser(AbstractUser):
    pass


class Graduate(models.Model):
    baseuser = models.OneToOneField(
        'BaseUser',
        on_delete=models.CASCADE
    )


class Customer(models.Model):
    baseuser = models.OneToOneField(
        'BaseUser',
        on_delete=models.CASCADE
    )


class Specialist(models.Model):
    baseuser = models.OneToOneField(
        'BaseUser',
        on_delete=models.CASCADE
    )
