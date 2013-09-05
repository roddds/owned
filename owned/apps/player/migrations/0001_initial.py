# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SaveSlot'
        db.create_table(u'player_saveslot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('player', ['SaveSlot'])

        # Adding M2M table for field inventory on 'SaveSlot'
        m2m_table_name = db.shorten_name(u'player_saveslot_inventory')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('saveslot', models.ForeignKey(orm['player.saveslot'], null=False)),
            ('item', models.ForeignKey(orm['book.item'], null=False))
        ))
        db.create_unique(m2m_table_name, ['saveslot_id', 'item_id'])

        # Adding M2M table for field events on 'SaveSlot'
        m2m_table_name = db.shorten_name(u'player_saveslot_events')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('saveslot', models.ForeignKey(orm['player.saveslot'], null=False)),
            ('event', models.ForeignKey(orm['book.event'], null=False))
        ))
        db.create_unique(m2m_table_name, ['saveslot_id', 'event_id'])

        # Adding model 'Player'
        db.create_table(u'player_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='player', unique=True, to=orm['auth.User'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('player', ['Player'])

        # Adding M2M table for field save_slot on 'Player'
        m2m_table_name = db.shorten_name(u'player_player_save_slot')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('player', models.ForeignKey(orm['player.player'], null=False)),
            ('saveslot', models.ForeignKey(orm['player.saveslot'], null=False))
        ))
        db.create_unique(m2m_table_name, ['player_id', 'saveslot_id'])

        # Adding model 'Progress'
        db.create_table(u'player_progress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['player.Player'])),
            ('paragraph', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['book.Paragraph'])),
            ('save_slot', self.gf('django.db.models.fields.related.ForeignKey')(related_name='progress_save_slot', to=orm['player.SaveSlot'])),
        ))
        db.send_create_signal('player', ['Progress'])


    def backwards(self, orm):
        # Deleting model 'SaveSlot'
        db.delete_table(u'player_saveslot')

        # Removing M2M table for field inventory on 'SaveSlot'
        db.delete_table(db.shorten_name(u'player_saveslot_inventory'))

        # Removing M2M table for field events on 'SaveSlot'
        db.delete_table(db.shorten_name(u'player_saveslot_events'))

        # Deleting model 'Player'
        db.delete_table(u'player_player')

        # Removing M2M table for field save_slot on 'Player'
        db.delete_table(db.shorten_name(u'player_player_save_slot'))

        # Deleting model 'Progress'
        db.delete_table(u'player_progress')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'book.event': {
            'Meta': {'object_name': 'Event'},
            'happened': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.TextField', [], {})
        },
        'book.item': {
            'Meta': {'object_name': 'Item'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'has': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'item_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        'book.option': {
            'Meta': {'object_name': 'Option'},
            'event_requirements': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['book.Event']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_requirements': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['book.Item']", 'symmetrical': 'False', 'blank': 'True'}),
            'target': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'book.paragraph': {
            'Meta': {'object_name': 'Paragraph'},
            'adds_events': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'adds_events'", 'blank': 'True', 'to': "orm['book.Event']"}),
            'adds_items': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'adds_items'", 'blank': 'True', 'to': "orm['book.Item']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ending': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'options': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'options'", 'null': 'True', 'to': "orm['book.Option']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'player.player': {
            'Meta': {'object_name': 'Player'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'save_slot': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'player_save_slot'", 'symmetrical': 'False', 'to': "orm['player.SaveSlot']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'player'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        'player.progress': {
            'Meta': {'object_name': 'Progress'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paragraph': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['book.Paragraph']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['player.Player']"}),
            'save_slot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'progress_save_slot'", 'to': "orm['player.SaveSlot']"})
        },
        'player.saveslot': {
            'Meta': {'object_name': 'SaveSlot'},
            'events': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['book.Event']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['book.Item']", 'symmetrical': 'False'}),
            'progress': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['book.Paragraph']", 'through': "orm['player.Progress']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['player']