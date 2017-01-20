# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'XMLFeedAPI'
        db.create_table(u'OpenOrderUpAPI_xmlfeedapi', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order_number', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('receipt_transaction_number', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('pos_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'OpenOrderUpAPI', ['XMLFeedAPI'])


    def backwards(self, orm):
        # Deleting model 'XMLFeedAPI'
        db.delete_table(u'OpenOrderUpAPI_xmlfeedapi')


    models = {
        u'OpenOrderUpAPI.xmlfeedapi': {
            'Meta': {'ordering': "('order_number',)", 'object_name': 'XMLFeedAPI'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_number': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'pos_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'receipt_transaction_number': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['OpenOrderUpAPI']