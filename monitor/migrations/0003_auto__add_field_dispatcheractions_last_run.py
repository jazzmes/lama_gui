# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DispatcherActions.last_run'
        db.add_column('monitor_dispatcheractions', 'last_run',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DispatcherActions.last_run'
        db.delete_column('monitor_dispatcheractions', 'last_run')


    models = {
        'monitor.dispatcher': {
            'Meta': {'object_name': 'Dispatcher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'})
        },
        'monitor.dispatcheractions': {
            'Meta': {'object_name': 'DispatcherActions'},
            'dispatcher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['monitor.Dispatcher']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_run': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'monitor.provideragent': {
            'Meta': {'object_name': 'ProviderAgent'},
            'agent_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'})
        }
    }

    complete_apps = ['monitor']