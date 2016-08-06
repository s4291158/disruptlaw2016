from django.db import models
from disputes.states_table import STATES

from disputes.category_model import DisputeCategory, DisputeCategoryQuestion

import random


class Dispute(models.Model):
    customer1 = models.ForeignKey(
        'users.Customer',
        on_delete=models.CASCADE,
        related_name='customer1_dispute'
    )

    customer2 = models.ForeignKey(
        'users.Customer',
        on_delete=models.CASCADE,
        related_name='customer2_dispute',
        null=True,
        blank=True
    )

    alt_id = models.IntegerField(
        default=0,
        unique=True
    )
    title = models.CharField(
        max_length=40,
        default=''
    )
    times_created = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(
        choices=STATES,
        default=1
    )

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.make_alt_id()
        self.title = str(self.alt_id)

    def make_alt_id(self, length=8):
        lower = 10 ** (length - 1)
        upper = 10 ** length - 1

        alt_id = random.randint(lower, upper)
        while self.objects.filter(alt_id=alt_id).count() > 0:
            alt_id = random.randint(lower, upper)
        self.alt_id = alt_id


class DisputeMaterial(models.Model):
    dispute = models.OneToOneField(
        'Dispute',
        on_delete=models.CASCADE
    )

    customer = models.ForeignKey(
        'users.Customer',
        on_delete=models.CASCADE
    )

    text = models.TextField()

    class Meta:
        unique_together = ('dispute', 'customer')


class DisputeDocument(models.Model):
    dispute_material = models.ForeignKey(
        'DisputeMaterial',
        on_delete=models.CASCADE
    )

    file = models.FileField(upload_to='uploads/')
