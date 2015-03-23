# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ambassadors'
        db.create_table(u'Ambassadors_ambassadors', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('original_image_width', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('original_image_height', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('thumb_image_width', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('thumb_image_height', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('image', self.gf(u'django.db.models.fields.files.ImageField')(max_length=100)),
            ('min_free_cropping', self.gf(u'django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
        ))
        db.send_create_signal(u'Ambassadors', ['Ambassadors'])


    def backwards(self, orm):
        # Deleting model 'Ambassadors'
        db.delete_table(u'Ambassadors_ambassadors')


    models = {
        u'Ambassadors.ambassadors': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Ambassadors'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': (u'django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'min_free_cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'original_image_height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'original_image_width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'thumb_image_height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'thumb_image_width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['Ambassadors']