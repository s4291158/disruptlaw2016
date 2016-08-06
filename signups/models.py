from django.db import models


class SignUp(models.Model):
    email = models.EmailField()
    time_stamp = models.DateTimeField(auto_now_add=True)
