from django.db import models
from django.contrib.auth.models import User

class Meteor(models.Model):
    datum = models.DateField()
    vreme = models.TimeField()
    mesto = models.CharField(max_length=30)
    magnituda = models.IntegerField()
    dodat = models.DateTimeField(auto_now_add=True)
    menjan = models.DateTimeField(auto_now=True)
    posmatrac = models.ForeignKey(User, on_delete=models.CASCADE)