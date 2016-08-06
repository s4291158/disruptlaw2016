from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseUser(AbstractUser):
    def is_user_type(self, attribute):
        if hasattr(self, attribute):
            return True
        else:
            return False

    def is_graduate(self):
        self.is_user_type('graduate')

    def is_customer(self):
        self.is_user_type('customer')

    def is_specialist(self):
        self.is_user_type('specialist')


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
