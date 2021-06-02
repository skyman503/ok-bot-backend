from django.db import models

# Create your models here.
class DiscordUser(models.Model):
    id = models.CharField(max_length=20, null=False, primary_key=True)
    background = models.ImageField()
