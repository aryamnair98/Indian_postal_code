from django.db import models

# Create your models here.
class Postal(models.Model):
    Pincode=models.CharField(max_length=10)
    Area=models.CharField(max_length=255)
    Branch_type = models.CharField(max_length=255)
    Circle=models.CharField(max_length=255)
    District=models.CharField(max_length=255)
    Division=models.CharField(max_length=255)
    Region=models.CharField(max_length=255)
    State = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)


    def __str__(self):
        return self.code

class PostalAddress(models.Model):
    Place=models.CharField(max_length=255)
    Branch_type = models.CharField(max_length=255)
    Circle=models.CharField(max_length=255)
    District=models.CharField(max_length=255)
    Division=models.CharField(max_length=255)
    Region=models.CharField(max_length=255)
    State = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Pincode = models.CharField(max_length=10)


    def __str__(self):
        return self.Place
