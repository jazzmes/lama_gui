# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DispatcherActions'
        db.create_table('monitor_dispatcheractions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dispatcher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitor.Dispatcher'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('monitor', ['DispatcherActions'])


    def backwards(self, orm):
        # Deleting model 'DispatcherActions'
        db.delete_table('monitor_dispatcheractions')


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