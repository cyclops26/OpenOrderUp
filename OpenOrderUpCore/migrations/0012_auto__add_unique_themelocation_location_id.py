# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'ThemeLocation', fields ['location_id']
        db.create_unique('OpenOrderUpCore_themelocation', ['location_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ThemeLocation', fields ['location_id']
        db.delete_unique('OpenOrderUpCore_themelocation', ['location_id'])


    models = {
        'OpenOrderUpCore.order': {
            'Meta': {'ordering': "('order_up_datetime',)", 'object_name': 'Order'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'order_up_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['OpenOrderUpCore.Restaurant']"})
        },
        'OpenOrderUpCore.orderplugin': {
            'Meta': {'_ormbases': ['cms.CMSPlugin'], 'object_name': 'OrderPlugin'},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'primary_key': 'True', 'unique': 'True'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['OpenOrderUpCore.Restaurant']"})
        },
        'OpenOrderUpCore.restaurant': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Restaurant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'order_router_ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'order_up_screen': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Page']"}),
            'reset_orders_nightly': ('django.db.models.fields.BooleanField', [], {})
        },
        'OpenOrderUpCore.theme': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Theme'},
            'background_color': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'background_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '250', 'blank': 'True'}),
            'background_repeat_x': ('django.db.models.fields.BooleanField', [], {}),
            'background_repeat_y': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '250', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['OpenOrderUpCore.ThemeLocation']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'OpenOrderUpCore.themefooterplugin': {
            'Meta': {'_ormbases': ['cms.CMSPlugin'], 'object_name': 'ThemeFooterPlugin'},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'primary_key': 'True', 'unique': 'True'}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['OpenOrderUpCore.Theme']"})
        },
        'OpenOrderUpCore.themeheaderplugin': {
            'Meta': {'_ormbases': ['cms.CMSPlugin'], 'object_name': 'ThemeHeaderPlugin'},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'primary_key': 'True', 'unique': 'True'}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['OpenOrderUpCore.Theme']"})
        },
        'OpenOrderUpCore.themelocation': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ThemeLocation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.page': {
            'Meta': {'unique_together': "(('publisher_is_draft', 'application_namespace'), ('reverse_id', 'site', 'publisher_is_draft'))", 'ordering': "('tree_id', 'lft')", 'object_name': 'Page'},
            'application_namespace': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'application_urls': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'changed_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'True'}),
            'is_home': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'languages': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'limit_visibility_in_menu': ('django.db.models.fields.SmallIntegerField', [], {'db_index': 'True', 'blank': 'True', 'default': 'None', 'null': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'navigation_extenders': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'blank': 'True', 'null': 'True', 'to': "orm['cms.Page']"}),
            'placeholders': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['cms.Placeholder']"}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'blank': 'True', 'null': 'True'}),
            'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'blank': 'True', 'null': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'null': 'True', 'to': "orm['cms.Page']", 'unique': 'True'}),
            'reverse_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'revision_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'djangocms_pages'", 'to': "orm['sites.Site']"}),
            'soft_root': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "'INHERIT'"}),
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
            'Meta': {'db_table': "'django_site'", 'ordering': "('domain',)", 'object_name': 'Site'},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['OpenOrderUpCore']