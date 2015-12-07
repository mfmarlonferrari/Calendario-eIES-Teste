# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0003_auto_20151205_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horario',
            name='qualPauta',
        ),
        migrations.RemoveField(
            model_name='pauta',
            name='qualDisciplina',
        ),
        migrations.RemoveField(
            model_name='pauta',
            name='qualProfessor',
        ),
        migrations.RemoveField(
            model_name='pauta',
            name='qualSala',
        ),
        migrations.RemoveField(
            model_name='pauta',
            name='qualTurma',
        ),
        migrations.AddField(
            model_name='disciplina',
            name='sala',
            field=models.ForeignKey(default=1, to='calendario.sala'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='disciplina',
            name='turma',
            field=models.ForeignKey(default=1, to='calendario.turma'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='horario',
        ),
        migrations.DeleteModel(
            name='pauta',
        ),
    ]
