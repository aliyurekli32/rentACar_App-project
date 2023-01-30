from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Car, Reservation
from car.serializers import CarSerializers, ReservationSerializer
from .permissions import IsStaffOrReadOnly
from django.db.models import Q
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CarView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializers
    permission_classes=[IsStaffOrReadOnly,]
    
    def get_queryset(self):
       
        if self.request.user.is_staff:
            queryset = super().get_queryset()
        else:
            queryset= super().get_queryset().filter(availability= True)
        start = self.request.query_params.get('start')
        # print(start)
        end = self.request.query_params.get('end')
        # print(end)
        
        if start is not None or end is not None:
            cond1= Q(start_date__lt=end)
            cond2 = Q(end_date__gt=start)
            not_available = Reservation.objects.filter(cond1 & cond2).values_list('car_id', flat=True)
            queryset = queryset.exclude(id__in = not_available)
        
        
        return queryset
    
    # def get_serializer_class(self):
    #     if self.request.user.is_staff:
    #             return CarStaffSerializer
    #     return super().get_serializer_class()
    
class ReservationView(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated,]
        
    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return super().get_queryset().filter(customer=self.request.user)
    
class ReservationDetailview(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
               
            