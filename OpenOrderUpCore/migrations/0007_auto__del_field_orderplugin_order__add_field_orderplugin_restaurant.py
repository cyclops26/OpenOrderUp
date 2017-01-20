# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'OrderPlugin.order'
        db.delete_column('OpenOrderUpCore_orderplugin', 'order_id')

        # Adding field 'OrderPlugin.restaurant'
        db.add_column('OpenOrderUpCore_orderplugin', 'restaurant',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['OpenOrderUpCore.Restaurant'], default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'OrderPlugin.order'
        db.add_column('OpenOrderUpCore_orderplugin', 'order',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['OpenOrderUpCore.Order'], default=1),
                      keep_default=False)

        # Deleting field 'OrderPlugin.restaurant'
        db.delete_column('OpenOrderUpCore_orderplugin', 'restaurant_id')


    models = {
        'OpenOrderUpCore.order': {
            'Meta': {'object_name': 'Order', 'ordering': "('order_up_datetime',)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'order_up_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['OpenOrderUpCore.Restaurant']"})
        },
        'OpenOrderUpCore.orderplugin': {
            'Meta': {'object_name': 'OrderPlugin', '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['OpenOrderUpCore.Restaurant']"})
        },
        'OpenOrderUpCore.restaurant': {
            'Meta': {'object_name': 'Restaurant', 'ordering': "('name',)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'order_router_ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'order_up_screen': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Page']"}),
            'reset_orders_nightly': ('django.db.models.fields.BooleanField', [], {})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['cms.CMSPlugin']", 'null': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.page': {
            'Meta': {'unique_together': "(('publisher_is_draft', 'application_namespace'), ('reverse_id', 'site', 'publisher_is_draft'))", 'object_name': 'Page', 'ordering': "('tree_id', 'lft')"},
            'application_namespace': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'application_urls': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'changed_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'True'}),
            'is_home': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'languages': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'limit_visibility_in_menu': ('django.db.models.fields.SmallIntegerField', [], {'db_index': 'True', 'blank': 'True', 'default': 'None', 'null': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'navigation_extenders': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'blank': 'True', 'max_length': '80', 'null': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['cms.Page']", 'null': 'True', 'related_name': "'children'"}),
            'placeholders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cms.Placeholder']", 'symmetrical': 'False'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'blank': 'True', 'null': 'True'}),
            'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'blank': 'True', 'null': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['cms.Page']", 'null': 'True', 'related_name': "'publisher_draft'"}),
            'reverse_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'blank': 'True', 'max_length': '40', 'null': 'True'}),
            'revision_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']", 'related_name': "'djangocms_pages'"}),
            'soft_root': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'INHERIT'", 'max_length': '100'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'xframe_options': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'})
        },
        'sites.site': {
            'Meta': {'object_name': 'Site', 'db_table': "'django_site'", 'ordering': "('domain',)"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['OpenOrderUpCore']