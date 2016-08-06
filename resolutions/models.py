from django.db import models


class Resolution(models.Model):
    dispute = models.ForeignKey(
        'disputes.Dispute',
        on_delete=models.CASCADE
    )

    graduate_set = models.ManyToManyField(
        'users.Graduate',
    )

    specialist = models.ForeignKey(
        'users.Specialist',
        null=True,
        blank=True
    )

    time_created = models.DateTimeField(auto_now_add=True)


class ResolutionDocuments(models.Model):
    resolution = models.OneToOneField(
        'Resolution',
        on_delete=models.CASCADE
    )

    file = models.FileField(upload_to='uploads/')
