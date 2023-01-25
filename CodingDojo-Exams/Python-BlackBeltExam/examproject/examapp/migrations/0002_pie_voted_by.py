# Generated by Django 4.1.5 on 2023-01-17 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pie',
            name='voted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pie_voted', to='examapp.user'),
        ),
    ]