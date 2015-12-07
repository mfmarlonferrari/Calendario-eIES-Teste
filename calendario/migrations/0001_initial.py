# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeAluno', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='disciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horarioDisciplina', models.DateTimeField()),
                ('nomeDisciplina', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dataInicial', models.DateTimeField()),
                ('dataFinal', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='pauta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qualDisciplina', models.ForeignKey(to='calendario.disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeProfessor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sala',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeSala', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='turma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeTurma', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='pauta',
            name='qualProfessor',
            field=models.ForeignKey(to='calendario.professor'),
        ),
        migrations.AddField(
            model_name='pauta',
            name='qualSala',
            field=models.ForeignKey(to='calendario.sala'),
        ),
        migrations.AddField(
            model_name='pauta',
            name='qualTurma',
            field=models.ForeignKey(to='calendario.turma'),
        ),
        migrations.AddField(
            model_name='horario',
            name='qualPauta',
            field=models.ForeignKey(to='calendario.pauta'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='professor',
            field=models.ForeignKey(to='calendario.professor'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='turma',
            field=models.ForeignKey(to='calendario.turma'),
        ),
    ]
