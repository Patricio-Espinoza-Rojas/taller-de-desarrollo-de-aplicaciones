# Generated by Django 4.2.6 on 2023-12-04 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receta',
            name='doctor',
        ),
        migrations.AlterField(
            model_name='receta',
            name='medicamentos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinicaApp.medicamentos'),
        ),
    ]
