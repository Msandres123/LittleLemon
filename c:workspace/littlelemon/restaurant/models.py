from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=0)
    booking_date = models.DateTimeField()

class Menu(models.Model):
   title = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   inventory = models.IntegerField(default=0) 

   def __str__(self):
      return self.title