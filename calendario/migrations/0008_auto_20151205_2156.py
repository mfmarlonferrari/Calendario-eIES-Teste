# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0007_auto_20151205_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='turma',
        ),
        migrations.AddField(
            model_name='aluno',
            name='turma',
            field=models.ForeignKey(default=1, to='calendario.turma'),
            preserve_default=False,
        ),
    ]
