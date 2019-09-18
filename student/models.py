from django.db import models

# Create your models here.
class stud(models.Model):
    naam = models.CharField(max_length= 100, null = False, blank=False)
    roll = models.IntegerField(unique=True)
    sem = models.IntegerField()

    def __str__(self):
        return str(self.roll)

