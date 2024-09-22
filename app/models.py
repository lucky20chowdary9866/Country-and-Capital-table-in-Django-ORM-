from django.db import models

# Create your models here.
class Country(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name
class Captial(models.Model):
    name=models.CharField(max_length=100)
    country=models.OneToOneField(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

