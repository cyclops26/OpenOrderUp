from django.db import models
from datetime import datetime, tzinfo, timedelta
from django.utils import timezone
from cms.models.pluginmodel import CMSPlugin
import pytz

class Restaurant(models.Model):
    GREY = 'btn-default'
    BLUE = 'btn-primary'
    GREEN = 'btn-success'
    LIGHT_BLUE = 'btn-info'
    ORANGE = 'btn-warning'
    RED = 'btn-danger'
    TRANSPARENT = 'btn-link'
    THEME_ORDER_NUMBER_SCHEME = (
        (GREY, 'Grey'),
        (BLUE, 'Blue'),
        (GREEN, 'Green'),
        (LIGHT_BLUE, 'Light Blue'),
        (ORANGE, 'Orange'),
        (RED, 'Red'),
        (TRANSPARENT, 'Transparent'),
    )
    name = models.CharField(max_length=250)
    fancy_name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=100)
    order_router_ip = models.GenericIPAddressField()
    order_up_screen = models.ForeignKey('cms.page', limit_choices_to={'is_home': False, 'publisher_is_draft': False})
    order_color = models.CharField(max_length=250,choices=THEME_ORDER_NUMBER_SCHEME)
    reset_orders_nightly = models.BooleanField()
    reset_orders_minute_interval = models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return '%s [Order Router: %s]' % (self.name,self.order_router_ip)
    
    class Meta:
        ordering = ('name',)

class PosDevice(models.Model):
    name = models.CharField(max_length=250)
    restaurant = models.ForeignKey(Restaurant)

    def __str__(self):
        return '%s [Restaurant: %s]' % (self.name,self.restaurant.name)

class Order(models.Model):
    number = models.IntegerField()
    restaurant = models.ForeignKey('Restaurant')
    order_up_datetime = models.DateTimeField()

    def __str__(self):
        return '%s: %s [%s]' % (self.restaurant,self.number,self.order_up_datetime.astimezone(pytz.timezone("America/New_York")))

    class Meta:
        ordering = ('order_up_datetime',)

    def last_x_minutes(self):
        if self.order_up_datetime >= timezone.now()-timedelta(seconds=30):
            output = '.5'
        elif self.order_up_datetime >= timezone.now()-timedelta(minutes=1):
            output = '1'
        elif self.order_up_datetime >= timezone.now()-timedelta(minutes=2):
            output = '2'
        elif self.order_up_datetime >= timezone.now()-timedelta(minutes=5):
            output = '5'
        else:
            output = '0'
        return output

    def order_up_datetime_local(self):
        return self.order_up_datetime.astimezone(pytz.timezone("America/New_York"))

class OrderPlugin(CMSPlugin):
    restaurant = models.ForeignKey('Restaurant')

class Theme(models.Model):
    HEADER = 'HEADER'
    FOOTER = 'FOOTER'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    THEME_LOCATIONS = (
        (HEADER, 'Header'),
        (FOOTER, 'Footer'),
        (LEFT, 'Left Side'),
        (RIGHT, 'Right Side'),
    )
    LIGHT = 'LIGHT'
    DARK = 'DARK'
    THEME_BACKGROUND_SCHEME = (
        (LIGHT, 'Light'),
        (DARK, 'Dark'),
    )
    GREY = 'btn-default'
    BLUE = 'btn-primary'
    GREEN = 'btn-success'
    LIGHT_BLUE = 'btn-info'
    ORANGE = 'btn-warning'
    RED = 'btn-danger'
    TRANSPARENT = 'btn-link'
    THEME_ORDER_NUMBER_SCHEME = (
        (GREY, 'Grey'),
        (BLUE, 'Blue'),
        (GREEN, 'Green'),
        (LIGHT_BLUE, 'Light Blue'),
        (ORANGE, 'Orange'),
        (RED, 'Red'),
        (TRANSPARENT, 'Transparent'),
    )
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250,choices=THEME_LOCATIONS)
    image = models.ImageField(upload_to='custom/images/uploaded',blank=True,max_length=250)
    text = models.TextField(blank=True)
    background_color = models.CharField(max_length=10,blank=True)
    background_image = models.ImageField(upload_to='custom/images/uploaded',blank=True,max_length=250)
    background_repeat_x = models.BooleanField()
    background_repeat_y = models.BooleanField()
    background_scheme = models.CharField(max_length=250,choices=THEME_BACKGROUND_SCHEME)

    def __str__(self):
        return '%s [%s]' % (self.name,self.location)

    class Meta:
        ordering = ('name',)

class Schedule(models.Model):
    WEEKDAYS = [
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday"),
    ]
    restaurant = models.ForeignKey(Restaurant)
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        ordering = ['restaurant', 'weekday', 'from_hour']

    def __str__(self):
        return '%s: %s (%s - %s)' % (self.restaurant.name,self.weekday,self.from_hour,self.to_hour)

class ThemeHeaderPlugin(CMSPlugin):
    theme = models.ForeignKey('Theme', limit_choices_to={'location': 'HEADER'})

class ThemeFooterPlugin(CMSPlugin):
    theme = models.ForeignKey('Theme', limit_choices_to={'location': 'FOOTER'})

class ThemeLeftPlugin(CMSPlugin):
    theme = models.ForeignKey('Theme', limit_choices_to={'location': 'LEFT'})

class ThemeRightPlugin(CMSPlugin):
    theme = models.ForeignKey('Theme', limit_choices_to={'location': 'RIGHT'})

