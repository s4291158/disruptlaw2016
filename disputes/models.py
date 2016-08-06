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

    def is_assigned(self):
        if self.graduate_set.all().count() > 0:
            return True
        else:
            return False


class DisputeMaterial(models.Model):
    dispute = models.ForeignKey(
        'Dispute',
        on_delete=models.CASCADE
    )

    customer = models.ForeignKey(
        'users.Customer',
        on_delete=models.CASCADE
    )


class DisputeDocument(models.Model):
    dispute_material = models.ForeignKey(
        'DisputeMaterial',
        on_delete=models.CASCADE
    )

    file = models.FileField(upload_to='uploads/')
