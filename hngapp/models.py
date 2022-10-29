from email.policy import default
from django.db import models


# Create your models here.
class hng (models.Model):
    slackUsername = models.CharField(max_length = 250)
    backend = models.BooleanField(default = False)
    age = models.IntegerField()
    bio = models.TextField()
    
    def __str__(self):
        return self.slackUsername