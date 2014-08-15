# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'People'
        db.create_table(u'ships_people', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('biog', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('birth_year', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'ships', ['People'])

        # Adding M2M table for field ships on 'People'
        m2m_table_name = db.shorten_name(u'ships_people_ships')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('people', models.ForeignKey(orm[u'ships.people'], null=False)),
            ('ship', models.ForeignKey(orm[u'ships.ship'], null=False))
        ))
        db.create_unique(m2m_table_name, ['people_id', 'ship_id'])


    def backwards(self, orm):
        # Deleting model 'People'
        db.delete_table(u'ships_people')

        # Removing M2M table for field ships on 'People'
        db.delete_table(db.shorten_name(u'ships_people_ships'))


    models = {
        u'ships.builder': {
            'Meta': {'object_name': 'Builder', '_ormbases': [u'ships.Company']},
            u'company_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ships.Company']", 'unique': 'True', 'primary_key': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'ships.company': {
            'Meta': {'object_name': 'Company'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ships.link': {
            'Meta': {'object_name': 'Link'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ships.othername': {
            'Meta': {'object_name': 'OtherName'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ships.owner': {
            'Meta': {'object_name': 'Owner', '_ormbases': [u'ships.Company']},
            'business': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'company_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ships.Company']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'ships.people': {
            'Meta': {'object_name': 'People'},
            'biog': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birth_year': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ships': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['ships.Ship']", 'null': 'True', 'blank': 'True'})
        },
        u'ships.ship': {
            'Meta': {'object_name': 'Ship'},
            'breadth_in_feet': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'build_year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'built_for': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'draft_in_feet': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'drive_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'history': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_in_feet': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'links': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ships.Link']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'other_names': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ships.OtherName']", 'null': 'True', 'blank': 'True'}),
            'previous_owners': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ships.Owner']", 'null': 'True', 'blank': 'True'}),
            'ship_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'yard_no': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'})
        }
    }

    complete_apps = ['ships']