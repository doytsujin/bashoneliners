# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-08 21:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AlternativeOneLiner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='HackerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.SlugField(blank=True, null=True, unique=True)),
                ('twitter_name', models.SlugField(blank=True, null=True)),
                ('blog_url', models.URLField(blank=True, null=True, verbose_name='Blog URL')),
                ('homepage_url', models.URLField(blank=True, null=True, verbose_name='Homepage URL')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='OneLiner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=200)),
                ('line', models.TextField()),
                ('explanation', models.TextField()),
                ('limitations', models.TextField(blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('was_tweeted', models.BooleanField(default=False)),
                ('created_dt', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
                'get_latest_by': 'pk',
            },
        ),
        migrations.CreateModel(
            name='OneLinerTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oneliner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneliners.OneLiner')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0)),
                ('created_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('oneliner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneliners.OneLiner')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='onelinertag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneliners.Tag'),
        ),
        migrations.AddField(
            model_name='alternativeoneliner',
            name='alternative',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_set', to='oneliners.OneLiner'),
        ),
        migrations.AddField(
            model_name='alternativeoneliner',
            name='oneliner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneliners.OneLiner'),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('user', 'oneliner')]),
        ),
        migrations.AlterUniqueTogether(
            name='alternativeoneliner',
            unique_together=set([('alternative', 'oneliner')]),
        ),
    ]