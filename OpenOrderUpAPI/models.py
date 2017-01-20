from django.db import models
from datetime import datetime
from cms.models.pluginmodel import CMSPlugin

class XMLFeedAPI(models.Model):
    order_number = models.CharField(max_length=250)
    receipt_transaction_number = models.CharField(max_length=250)
    pos_name = models.CharField(max_length=250)
    order_router = models.CharField(max_length=50)
    
    def __str__(self):
        return '%s [POS: %s]' % (self.order_number,self.pos_name)
    
    class Meta:
        ordering = ('order_number',)


