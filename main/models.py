from django.db import models
class Account(models.Model):
    rank = models.PositiveIntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    percentage = models.CharField(max_length=240, null=True, blank=True)
    balance = models.CharField(max_length=240, null=True, blank=True)

    class Meta:
        ordering = ["-rank"]

    def __str__(self):
        return self.balance