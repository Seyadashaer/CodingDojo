# Generated by Django 4.1.5 on 2023-01-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0004_remove_user_voted_pie_voted_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pie',
            name='voted_by',
        ),
        migrations.AddField(
            model_name='pie',
            name='users_who_vote2',
            field=models.ManyToManyField(related_name='voted_pies2', to='examapp.user'),
        ),
    ]
