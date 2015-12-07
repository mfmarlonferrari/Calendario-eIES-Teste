# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0002_auto_20151201_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='repeteDisciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qualDia', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='horarioFinal',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='horarioInicio',
            field=models.TimeField(),
        ),
        migrations.AddField(
            model_name='repetedisciplina',
            name='qualDisciplina',
            field=models.ForeignKey(to='calendario.disciplina'),
        ),
    ]
