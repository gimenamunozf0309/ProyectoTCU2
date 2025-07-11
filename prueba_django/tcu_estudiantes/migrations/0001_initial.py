# Generated by Django 4.2.22 on 2025-06-07 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TCUEstudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('identificacion', models.CharField(max_length=20)),
                ('carnet', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
                ('lugar_tcu', models.CharField(max_length=200)),
                ('encargado', models.CharField(max_length=100)),
                ('fecha_solicitud', models.DateField()),
                ('estado', models.CharField(choices=[('En revisión', 'En revisión'), ('Pendiente', 'Pendiente'), ('Rechazado', 'Rechazado'), ('Aprobado', 'Aprobado')], default='Pendiente', max_length=20)),
                ('observaciones', models.TextField(blank=True)),
                ('documento', models.FileField(blank=True, null=True, upload_to='documentos_tcu/')),
            ],
        ),
    ]
