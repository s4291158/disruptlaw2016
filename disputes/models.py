from django.db import models


class Dispute(models.Model):
    customer1 = models.ForeignKey(
        'users.Customer',
        on_delete=models.CASCADE,
        related_name='dispute_customer1'
    )

    customer2 = models.ForeignKey(
        'users.Customer',
        on_delete=models.CASCADE,
        related_name='dispute_customer2'
    )

    title = models.CharField(max_length=40)
    text = models.TextField()
    times_created = models.DateTimeField(auto_now_add=True)
