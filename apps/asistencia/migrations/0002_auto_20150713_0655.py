# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notas', '0001_initial'),
        ('matricula', '0002_auto_20150713_0655'),
    ]

    operations = [
        migrations.AddField(
            model_name='docente',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cargaacademica',
            name='asignatura',
            field=models.ForeignKey(to='notas.Asignatura'),
        ),
        migrations.AddField(
            model_name='cargaacademica',
            name='aula',
            field=models.ForeignKey(to='asistencia.Aula'),
        ),
        migrations.AddField(
            model_name='cargaacademica',
            name='docente',
            field=models.ForeignKey(to='asistencia.Docente'),
        ),
        migrations.AddField(
            model_name='cargaacademica',
            name='horario',
            field=models.ForeignKey(to='asistencia.Horario'),
        ),
        migrations.AddField(
            model_name='asistenciadocente',
            name='carga_academica',
            field=models.ForeignKey(to='asistencia.CargaAcademica'),
        ),
        migrations.AddField(
            model_name='asistenciaalumno',
            name='asignatura',
            field=models.ForeignKey(to='notas.Asignatura'),
        ),
        migrations.AddField(
            model_name='asistenciaalumno',
            name='docente',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='asistenciaalumno',
            name='matricula',
            field=models.ForeignKey(to='matricula.Matricula'),
        ),
    ]