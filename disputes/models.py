from django.db import models
from django.db.utils import IntegrityError

from disputes.states_table import STATES
from disputes.category_questions import category_choices

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

    category = models.IntegerField(
        choices=category_choices
    )

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.make_alt_id()
        self.title = str(self.alt_id)

    def make_alt_id(self, length=8):
        lower = 10 ** (length - 1)
        upper = 10 ** length - 1

        while True:
            self.alt_id = random.randint(lower, upper)
            try:
                self.save()
                break
            except IntegrityError:
                pass


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


class DisputeQNA(models.Model):
    dispute_material = models.ForeignKey(
        'DisputeMaterial',
        on_delete=models.CASCADE
    )

    question = models.TextField()
    answer = models.TextField()
