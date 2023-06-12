from django.db import models
from Login.models import User

class Reminder(models.Model):
    topic = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    