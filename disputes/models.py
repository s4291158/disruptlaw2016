from django.db import models

from disputes.states_table import STATES


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

    title = models.CharField(max_length=40)
    times_created = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(
        choices=STATES,
        default=1
    )

    def finalise(self, customer2):
        self.customer2 = customer2
        self.state = 3
        self.save()


class DisputeMaterial(models.Model):
    dispute = models.ForeignKey(
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

    def save(self, **kwargs):
        super(self.__class__, self).save(**kwargs)
        conditions = [
            self.dispute_material.dispute.customer1 ==
            self.dispute_material.customer

        ]
