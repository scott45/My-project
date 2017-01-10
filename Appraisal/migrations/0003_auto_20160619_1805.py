# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Appraisal', '0002_auto_20160614_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('Name', models.CharField(max_length=30)),
                ('Department_logo', models.FileField(upload_to='')),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('Branch', models.CharField(max_length=30)),
                ('is_favorite', models.BooleanField(default=False)),
                ('Names', models.ForeignKey(max_length=30, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('Title', models.CharField(max_length=30)),
                ('is_favorite', models.BooleanField(default=False)),
                ('Department', models.ForeignKey(to='Appraisal.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('About_me', models.CharField(max_length=150)),
                ('Strength_of_your_department', models.CharField(max_length=200)),
                ('Weakness_of_your_department', models.CharField(max_length=200)),
                ('Personal_challenges_about_work', models.CharField(max_length=150)),
                ('Comment_about_work_relations_at_Anppcan', models.CharField(max_length=200)),
                ('Shortly_advise_Anppcan_on_what_you_feel_must_change', models.CharField(max_length=200)),
                ('Best_Employee_or_Co_worker', models.ForeignKey(to='Appraisal.Employee')),
                ('Department', models.ForeignKey(to='Appraisal.Department')),
                ('Title', models.ForeignKey(to='Appraisal.Post')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='Leader',
            field=models.ForeignKey(to='Appraisal.Employee'),
        ),
    ]
