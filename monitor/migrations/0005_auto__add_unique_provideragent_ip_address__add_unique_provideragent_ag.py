# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'ProviderAgent', fields ['ip_address']
        db.create_unique('monitor_provideragent', ['ip_address'])

        # Adding unique constraint on 'ProviderAgent', fields ['agent_id']
        db.create_unique('monitor_provideragent', ['agent_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ProviderAgent', fields ['agent_id']
        db.delete_unique('monitor_provideragent', ['agent_id'])

        # Removing unique constraint on 'ProviderAgent', fields ['ip_address']
        db.delete_unique('monitor_provideragent', ['ip_address'])


    models = {
        'monitor.dispatcher': {
            'Meta': {'object_name': 'Dispatcher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'})
        },
        'monitor.dispatcheraction': {
            'Meta': {'object_name': 'DispatcherAction'},
            'dispatcher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['monitor.Dispatcher']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_run': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        },
        'monitor.provideragent': {
            'Meta': {'object_name': 'ProviderAgent'},
            'agent_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'unique': 'True'}),
            'last_seen': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['monitor']