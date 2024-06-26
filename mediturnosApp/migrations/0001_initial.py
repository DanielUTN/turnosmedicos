# Generated by Django 5.0.6 on 2024-05-24 22:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=250, verbose_name='Especialidad')),
                ('descripcion', models.TextField(default='', max_length=250, verbose_name='Descripción de la especialidad')),
                ('imagen', models.ImageField(upload_to='media')),
            ],
            options={
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=150, verbose_name='Email')),
                ('dni', models.IntegerField(unique=True, verbose_name='Dni')),
                ('matricula', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Matrícula')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MedicoEspecialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.ForeignKey(db_column='especialidad_id', on_delete=django.db.models.deletion.CASCADE, to='mediturnosApp.especialidad')),
                ('medico', models.ForeignKey(db_column='matricula', on_delete=django.db.models.deletion.CASCADE, to='mediturnosApp.medico')),
            ],
            options={
                'verbose_name_plural': 'Medico especialidades',
            },
        ),
        migrations.AddField(
            model_name='medico',
            name='especialidades',
            field=models.ManyToManyField(through='mediturnosApp.MedicoEspecialidad', to='mediturnosApp.especialidad'),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=150, verbose_name='Email')),
                ('dni', models.IntegerField(unique=True, verbose_name='Dni')),
                ('historia_clinica', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='Historia Clínica')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('cancelado', models.BooleanField()),
                ('historia_clinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mediturnosApp.paciente')),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mediturnosApp.medico')),
            ],
            options={
                'verbose_name': 'Turno',
                'verbose_name_plural': 'Turnos',
            },
        ),
    ]
