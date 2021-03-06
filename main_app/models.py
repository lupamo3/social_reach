from django.db import models


class Niche(models.Model):
    name = models.CharField(max_length=40)
    info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
