# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appraisal', '0003_auto_20160619_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('About_me', models.CharField(max_length=150)),
                ('Strength_of_your_department', models.CharField(max_length=300)),
                ('Weakness_of_your_department', models.CharField(max_length=300)),
                ('Personal_challenges_about_work', models.CharField(max_length=350)),
                ('Comment_about_work_relations_at_Anppcan', models.CharField(max_length=300)),
                ('Shortly_advise_Anppcan_on_what_you_feel_must_change', models.CharField(max_length=300)),
                ('Best_Employee_or_Co_worker', models.ForeignKey(to='Appraisal.Employee')),
                ('Department', models.ForeignKey(to='Appraisal.Department')),
                ('Title', models.ForeignKey(to='Appraisal.Post')),
            ],
        ),
        migrations.RemoveField(
            model_name='questions',
            name='Best_Employee_or_Co_worker',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='Department',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='Title',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]
