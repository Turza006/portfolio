from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100,null=True,blank=True)
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary