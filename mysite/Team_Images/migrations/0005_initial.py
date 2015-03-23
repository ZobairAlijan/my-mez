# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CropImageExample'
        db.create_table(u'Team_Images_cropimageexample', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('original_image_width', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('original_image_height', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('thumb_image_width', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('thumb_image_height', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('image', self.gf(u'django.db.models.fields.files.ImageField')(max_length=100)),
            ('min_free_cropping', self.gf(u'django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
            ('facebook_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('twitter_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('tumblr_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('github_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('google_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('OSF_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('linkedin_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('personal_Email', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('personal_web', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'Team_Images', ['CropImageExample'])


    def backwards(self, orm):
        # Deleting model 'CropImageExample'
        db.delete_table(u'Team_Images_cropimageexample')


    models = {
        u'Team_Images.cropimageexample': {
            'Meta': {'ordering': "('name',)", 'object_name': 'CropImageExample'},
            'OSF_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'facebook_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'github_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'google_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': (u'django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'linkedin_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'min_free_cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'original_image_height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'original_image_width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'personal_Email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'personal_web': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'thumb_image_height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'thumb_image_width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'tumblr_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'twitter_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['Team_Images']