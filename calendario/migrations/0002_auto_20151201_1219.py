# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disciplina',
            old_name='horarioDisciplina',
            new_name='horarioFinal',
        ),
        migrations.AddField(
            model_name='disciplina',
            name='horarioInicio',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 1, 14, 19, 11, 500000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
