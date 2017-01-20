# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Restaurant'
        db.create_table('OpenOrderUpCore_restaurant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('order_router_ip', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
        ))
        db.send_create_signal('OpenOrderUpCore', ['Restaurant'])


    def backwards(self, orm):
        # Deleting model 'Restaurant'
        db.delete_table('OpenOrderUpCore_restaurant')


    models = {
        'OpenOrderUpCore.restaurant': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Restaurant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'order_router_ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'})
        }
    }

    complete_apps = ['OpenOrderUpCore']