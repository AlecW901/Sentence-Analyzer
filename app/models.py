from django.db import models

# Create your models here.
class Sentence(models.Model):
    sentence=models.CharField(max_length=100,null=False,blank=False)
    