# Generated by Django 3.1.3 on 2020-11-23 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201122_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despacho',
            name='Orden_Compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.orden_compra', unique=True),
        ),
    ]
