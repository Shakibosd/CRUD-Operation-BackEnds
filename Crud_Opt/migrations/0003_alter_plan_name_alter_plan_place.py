# Generated by Django 5.0.6 on 2025-04-24 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crud_Opt', '0002_alter_plan_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='plan',
            name='place',
            field=models.CharField(max_length=500),
        ),
    ]
