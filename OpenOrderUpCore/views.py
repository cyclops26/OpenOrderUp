from django.shortcuts import render
from OpenOrderUpCore.models import *
from OpenOrderUpCore.serializers import *
from rest_framework import generics
from datetime import datetime, timedelta
import time
from django.utils import timezone

class OrderListAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):

        short_name = self.kwargs['restaurant']
        restaurant = Restaurant.objects.get(
            short_name=short_name
        )

        return Order.objects.filter(restaurant=restaurant,order_up_datetime__gte=timezone.now()-timedelta(minutes=5)).order_by('-order_up_datetime')[:50]

class OpenHoursTodayView(generics.ListAPIView):
    serializer_class = ScheduleSerializer
    
    def get_queryset(self):
        short_name = self.kwargs['restaurant']
        restaurant = Restaurant.objects.get(
            short_name=short_name
        )
        weekdays = {
            "MONDAY" : 1,
            "TUESDAY" : 2,
            "WEDNESDAY" : 3,
            "THURSDAY" : 4,
            "FRIDAY" : 5,
            "SATURDAY" : 6,
            "SUNDAY" : 7
        }
        now = datetime.now()
        day = now.strftime("%A").upper()
        weekday = weekdays[day]
        schedule = Schedule.objects.filter(restaurant=restaurant,weekday=weekday)
        return schedule

