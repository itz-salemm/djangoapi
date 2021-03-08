from django.db import models

# Create your models here.
class employees(models.Model):
    firstname = models.CharField(max_length=10)
    latsname = models.CharField(max_length=10)
    em_id = models.IntegerField()

    def __str__(self):
        return self.firstname
