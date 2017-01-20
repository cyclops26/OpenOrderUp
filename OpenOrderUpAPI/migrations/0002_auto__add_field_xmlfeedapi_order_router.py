# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'XMLFeedAPI.order_router'
        db.add_column(u'OpenOrderUpAPI_xmlfeedapi', 'order_router',
                      self.gf('django.db.models.fields.CharField')(default='10.64.60.30', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'XMLFeedAPI.order_router'
        db.delete_column(u'OpenOrderUpAPI_xmlfeedapi', 'order_router')


    models = {
        u'OpenOrderUpAPI.xmlfeedapi': {
            'Meta': {'ordering': "('order_number',)", 'object_name': 'XMLFeedAPI'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_number': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'order_router': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pos_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'receipt_transaction_number': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['OpenOrderUpAPI']