from django.db import models

from resolutions.states_table import STATES


class Resolution(models.Model):
    dispute = models.ForeignKey(
        'disputes.Dispute',
        on_delete=models.CASCADE
    )

    graduate = models.ForeignKey(
        'users.Graduate',
    )

    time_created = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(
        choices=STATES,
        default=1
    )


class ResolutionProposal(models.Model):
    resolution = models.OneToOneField(
        'Resolution',
        on_delete=models.CASCADE
    )

    file = models.FileField(upload_to='uploads/')
    time_created = models.DateTimeField(auto_now_add=True)


class ResolutionResolve(models.Model):
    resolution = models.OneToOneField(
        'Resolution',
        on_delete=models.CASCADE
    )

    specialist = models.ForeignKey(
        'users.Specialist'
    )

    file = models.FileField(upload_to='upload/')
    time_created = models.DateTimeField(auto_now_add=True)
