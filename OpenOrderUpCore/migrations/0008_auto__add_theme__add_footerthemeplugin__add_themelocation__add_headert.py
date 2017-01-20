# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Theme'
        db.create_table('OpenOrderUpCore_theme', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['OpenOrderUpCore.ThemeLocation'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(blank=True, max_length=250)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('OpenOrderUpCore', ['Theme'])

        # Adding model 'FooterThemePlugin'
        db.create_table('OpenOrderUpCore_footerthemeplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, to=orm['cms.CMSPlugin'], unique=True)),
            ('theme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['OpenOrderUpCore.Theme'])),
        ))
        db.send_create_signal('OpenOrderUpCore', ['FooterThemePlugin'])

        # Adding model 'ThemeLocation'
        db.create_table('OpenOrderUpCore_themelocation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('OpenOrderUpCore', ['ThemeLocation'])

        # Adding model 'HeaderThemePlugin'
        db.create_table('OpenOrderUpCore_headerthemeplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, to=orm['cms.CMSPlugin'], unique=True)),
            ('theme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['OpenOrderUpCore.Theme'])),
        ))
        db.send_create_signal('OpenOrderUpCore', ['HeaderThemePlugin'])


    def backwards(self, orm):
        # Deleting model 'Theme'
        db.delete_table('OpenOrderUpCore_theme')

        # Deleting model 'FooterThemePlugin'
        db.delete_table('OpenOrderUpCore_footerthemeplugin')

        # Deleting model 'ThemeLocation'
        db.delete_table('OpenOrderUpCore_themelocation')

        # Deleting model 'HeaderThemePlugin'
        db.delete_table('OpenOrderUpCore_headerthemeplugin')


    models = {
        'OpenOrderUpCore.footerthemeplugin': {
            'Meta': {'_ormbases': ['cms.CMSPlugin'], 'object_name': 'FooterThemePlugin'},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['cms.CMSPlugin']", 'unique': 'True'}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['OpenOrderUpCore.Theme']"})
        },
        'OpenOrderUpCore.headerthemeplugin': {
            'Meta': {'_ormbases': ['cms.CMSPlugin'], 'object_name': 'HeaderThemePlugin'},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['cms.CMSPlugin']", 'unique': 'True'}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['OpenOrderUpCore.Theme']"})
        },
        'OpenOrderUpCore.order': {
            'Meta': {'ordering': "('order_up_datetime',)", 'object_name': 'Order'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'order_up_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['OpenOrderUpCore.Restaurant']"})
        },
        'OpenOrderUpCore.orderplugin': {
            'Meta': {'_ormbases': ['cms.CMSPlugin'], 'object_name': 'OrderPlugin'},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['cms.CMSPlugin']", 'unique': 'True'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '250'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['OpenOrderUpCore.ThemeLocation']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'OpenOrderUpCore.themelocation': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ThemeLocation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
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
            'Meta': {'ordering': "('tree_id', 'lft')", 'unique_together': "(('publisher_is_draft', 'application_namespace'), ('reverse_id', 'site', 'publisher_is_draft'))", 'object_name': 'Page'},
            'application_namespace': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'application_urls': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'db_index': 'True', 'max_length': '200'}),
            'changed_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'True'}),
            'is_home': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'languages': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'limit_visibility_in_menu': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True', 'null': 'True', 'db_index': 'True', 'default': 'None'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'navigation_extenders': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'db_index': 'True', 'max_length': '80'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['cms.Page']"}),
            'placeholders': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['cms.Placeholder']"}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True', 'db_index': 'True'}),
            'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True', 'db_index': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'null': 'True', 'to': "orm['cms.Page']", 'unique': 'True'}),
            'reverse_id': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'db_index': 'True', 'max_length': '40'}),
            'revision_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'djangocms_pages'", 'to': "orm['sites.Site']"}),
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
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['OpenOrderUpCore']