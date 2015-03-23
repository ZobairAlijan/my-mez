# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pages'
        db.create_table(u'Main_page_pages', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('body', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'Main_page', ['Pages'])


    def backwards(self, orm):
        # Deleting model 'Pages'
        db.delete_table(u'Main_page_pages')


    models = {
        u'Main_page.pages': {
            'Meta': {'object_name': 'Pages'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['Main_page']