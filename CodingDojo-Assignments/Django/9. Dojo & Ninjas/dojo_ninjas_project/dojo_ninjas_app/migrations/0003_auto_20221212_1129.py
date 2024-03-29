# Generated by Django 2.2.4 on 2022-12-12 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0002_dojo_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dojo',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dojo',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dojo',
            name='state',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='ninja',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ninja',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
