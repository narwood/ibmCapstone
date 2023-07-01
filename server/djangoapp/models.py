from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return "Name: " + self.name + ", " + "Description: " + self.description



class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    dealer = models.IntegerField()
    TYPE_CHOICES = [('SE', 'Sedan'), ('SU', 'SUV'), ('WA', 'WAGON')]
    car_type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    year = models.DateField()

    def __str__(self):
        return "Make: " + str(self.make.name) + ", " + "Name: " + self.name + ", " + "Dealer: " + str(self.dealer) + ", " + "Type: " + self.car_type + ", " + "Year: " + str(self.year.year)


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
