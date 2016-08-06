from django.db import models


class Question(models.Model):
    customer = models.ForeignKey(
        'users.Customer',
        on_delete=models.CASCADE
    )

    text = models.TextField()
    times_created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE
    )

    student = models.ForeignKey(
        'users.Student',
        on_delete=models.CASCADE
    )

    text = models.TextField()
    times_created = models.DateTimeField(auto_now_add=True)
