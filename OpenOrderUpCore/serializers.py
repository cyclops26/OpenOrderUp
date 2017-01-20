from rest_framework import serializers
from OpenOrderUpCore.models import *

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('number', 'restaurant', 'order_up_datetime', 'order_up_datetime_local', 'last_x_minutes')

class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = ('restaurant','weekday','from_hour','to_hour')
