from rest_framework import serializers
from .models import Car,Reservation

class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'id',
            'plate_number',
            'brand',
            'model',
            'year',
            'gear',
            'rent_per_day',
            'availability'
        )