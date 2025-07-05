from django.db import models

# Create your models here.

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    species_applicable = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
