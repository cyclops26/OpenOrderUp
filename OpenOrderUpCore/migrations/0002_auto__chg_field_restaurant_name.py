# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Restaurant.name'
        db.alter_column('OpenOrderUpCore_restaurant', 'name', self.gf('django.db.models.fields.CharField')(max_length=250))

    def backwards(self, orm):

        # Changing field 'Restaurant.name'
        db.alter_column('OpenOrderUpCore_restaurant', 'name', self.gf('django.db.models.fields.TextField')())

    models = {
        'OpenOrderUpCore.restaurant': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Restaurant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'order_router_ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'})
        }
    }

    complete_apps = ['OpenOrderUpCore']