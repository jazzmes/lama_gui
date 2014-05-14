# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'DispatcherActions'
        db.delete_table('monitor_dispatcheractions')

        # Adding model 'DispatcherAction'
        db.create_table('monitor_dispatcheraction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dispatcher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitor.Dispatcher'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True)),
            ('last_run', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('monitor', ['DispatcherAction'])

        # Adding field 'ProviderAgent.last_seen'
        db.add_column('monitor_provideragent', 'last_seen',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, auto_now_add=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'DispatcherActions'
        db.create_table('monitor_dispatcheractions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_run', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('dispatcher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitor.Dispatcher'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('monitor', ['DispatcherActions'])

        # Deleting model 'DispatcherAction'
        db.delete_table('monitor_dispatcheraction')

        # Deleting field 'ProviderAgent.last_seen'
        db.delete_column('monitor_provideragent', 'last_seen')


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
            'agent_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'last_seen': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['monitor']