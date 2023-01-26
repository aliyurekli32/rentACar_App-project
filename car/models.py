from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Car(models.Model):
    GEAR = (
        ('a', 'automatic'),
        ('m', 'manuel')
    )
    plate_number = models.CharField(max_length=15, unique=True)
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=20)
    year = models.SmallIntegerField()
    gear = models.CharField(max_length=1, choices=GEAR)
    rent_per_day = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(1)]
    )
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.model} - {self.brand} - {self.plate_number}'

class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "customers")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="cars")
    start_date =models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return f"{self.customer} - {self.car} - start:{self.start_date} - end_date:{self.end_date}"
    
    class Meta:
        constraints =[
            models.UniqueConstraint(
                fields = ['customer', 'start_date', 'end_date'],name='user_rent_date'
            )
        ]