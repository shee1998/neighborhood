from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    n_occupants = models.CharField(max_length=100,blank=True)
    Admin = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Occupants(models.Model):
    profile_photo=models.ImageField(upload_to='images')
    name = models.ForeignKey(User)
    id_number= models.CharField(max_length=100)
    email=models.EmailField()
    neighborhood= models.ForeignKey(Neighborhood,on_delete=models.CASCADE)

    def __str__(self):
        return self.name.username


class Business(models.Model):
    business_name= models.CharField(max_length=100)
    owner= models.ForeignKey(User)
    b_email=models.EmailField()
    description=models.TextField()
    neighborhood= models.ForeignKey(Neighborhood,on_delete=models.CASCADE)

    def __str__(self):
        return self.business_name