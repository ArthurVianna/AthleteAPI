# Generated by Django 2.2.9 on 2020-02-02 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Athlete', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='age',
        ),
        migrations.AddField(
            model_name='participation',
            name='age',
            field=models.IntegerField(blank=True, help_text='Age of the athlete', null=True, verbose_name='Athlete age'),
        ),
    ]