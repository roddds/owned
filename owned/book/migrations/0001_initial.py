# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 18:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('image_filename', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('target', models.PositiveIntegerField()),
                ('excluding_events', models.ManyToManyField(blank=True, related_name='excludes_option', to='book.Event')),
                ('excluding_items', models.ManyToManyField(blank=True, related_name='excludes_option', to='book.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('is_ending', models.BooleanField(default=False)),
                ('adds_events', models.ManyToManyField(blank=True, related_name='adds_events', to='book.Event')),
                ('adds_items', models.ManyToManyField(blank=True, related_name='adds_items', to='book.Item')),
                ('removes_items', models.ManyToManyField(blank=True, related_name='removes_items', to='book.Item')),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='paragraph',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Paragraph'),
        ),
        migrations.AddField(
            model_name='option',
            name='required_events',
            field=models.ManyToManyField(blank=True, related_name='enables_option', to='book.Event'),
        ),
        migrations.AddField(
            model_name='option',
            name='required_items',
            field=models.ManyToManyField(blank=True, related_name='enables_option', to='book.Item'),
        ),
    ]