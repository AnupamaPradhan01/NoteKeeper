from django.db import models

class Notekeeper(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=300,blank=True, null=True, default="Some text")
