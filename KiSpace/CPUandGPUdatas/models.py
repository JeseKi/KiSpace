from django.db import models

# Create your models here.
class CPU(models.Model):
    name = models.CharField(max_length=100)
    performance_score = models.IntegerField()

    def __str__(self):
        return self.name
    
class GPU(models.Model):
    name = models.CharField(max_length=100)
    performance_score = models.IntegerField()

    def __str__(self):
        return self.name