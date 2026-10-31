from django.db import models


# Create your models here.
class Tour(models.Model):
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.DecimalField()

    def __str__(self):
        return f"ID:{self.id} : To {self.destination_country} From {self.origin_country} Number of nights : {self.number_of_nights} price : {self.price}"
