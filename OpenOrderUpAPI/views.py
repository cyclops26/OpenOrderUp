from django.shortcuts import render
from OpenOrderUpAPI.models import *
from OpenOrderUpAPI.serializers import *
from OpenOrderUpCore.models import *
from OpenOrderUpCore.serializers import *
from rest_framework import generics
import xml.etree.ElementTree as ET
from django.views.generic.edit import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.http import StreamingHttpResponse
from django.views.decorators.http import require_http_methods
import datetime

@require_http_methods(["GET", "POST"])
def NewOrderUp(request):
        timestamp = datetime.datetime.now()
        output = ""
        debug = ""
        data = []
        resp = StreamingHttpResponse()
        try:
            #debug = request
            router = request.META['REMOTE_ADDR']
            if not router:
                router = "0.0.0.0"
            xml = request.body
            transaction = ET.fromstring(xml)

            order_number = transaction[0].text
            receipt_transaction_number  = transaction[1].text 
            pos_name = transaction[2].text

            data = [order_number,receipt_transaction_number,pos_name,router]
            output = data
        except Exception as exception:
            data = []
            output = "Failed to read order | Exception: ", exception
            resp.status_code = "500"

        if data:
          if not "EPOS" in pos_name and not "ePOS" in pos_name and not "epos" in pos_name:
            try:
                order_up = XMLFeedAPI(order_number=order_number, receipt_transaction_number=receipt_transaction_number, pos_name=pos_name, order_router=router)
                order_up.save()
                output = "[" + router + "] Order written to database: ", output
                resp.status_code = "200"
            except Exception as exception:
                output = "Failed to write order to database | Exception: ", exception, " | ", output
                resp.status_code = "500"

            try:
                posdevice = PosDevice.objects.get(
                    name=pos_name
                )
                restaurant = Restaurant.objects.get(
                    #order_router_ip=router
                    id=posdevice.restaurant.id
                )
                if restaurant.id:
                    publish_order = Order(number=order_number, restaurant=restaurant, order_up_datetime=timestamp)
                    publish_order.save()
            except Exception as exception:
                output = "Failed to publish order to display | Exception: ", exception, " | ", output
                resp.status_code = "500"

        output = output, " | ", debug
        resp.streaming_content = output
        return resp
