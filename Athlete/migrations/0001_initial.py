# Generated by Django 2.2.9 on 2020-02-01 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the city', max_length=255, verbose_name='City name')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the event', max_length=255, verbose_name='Event name')),
            ],
        ),
        migrations.CreateModel(
            name='NOC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noc', models.CharField(help_text='National Olympic Committee 3 letter code', max_length=3, verbose_name='National Olympic Committee')),
                ('region', models.CharField(help_text='Country that the NOC represents', max_length=100, verbose_name='Country name')),
                ('notes', models.CharField(help_text='Notes about the NOC', max_length=255, verbose_name='Notes')),
            ],
        ),
        migrations.CreateModel(
            name='Olympics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the Olympics', max_length=255, verbose_name='Games name')),
                ('year', models.IntegerField(help_text='Year that the Olympics happened', verbose_name='Year')),
                ('Season', models.CharField(help_text='Season that the Olympics happened', max_length=6, verbose_name='Season')),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the sport', max_length=255, verbose_name='Sport name')),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medal', models.CharField(help_text='Medal that the participant received', max_length=10, verbose_name='Medal received')),
                ('team', models.CharField(help_text='Team of the participant', max_length=255, verbose_name='Team name')),
                ('city', models.ForeignKey(help_text='City that the event happened', on_delete=django.db.models.deletion.CASCADE, to='Athlete.City', verbose_name='City')),
                ('event', models.ForeignKey(help_text='Event that the athlete participated', on_delete=django.db.models.deletion.CASCADE, to='Athlete.Event', verbose_name='Event')),
                ('olympic', models.ForeignKey(help_text='Olympics related to the participation', on_delete=django.db.models.deletion.CASCADE, to='Athlete.Olympics', verbose_name='Olympics')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='sport',
            field=models.ForeignKey(help_text='Sport of this event', on_delete=django.db.models.deletion.CASCADE, to='Athlete.Sport', verbose_name='Sport'),
        ),
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the Athlete', max_length=255, verbose_name='Athlete name')),
                ('sex', models.CharField(help_text='Sex of the athlete', max_length=1, verbose_name='Athlete sex')),
                ('age', models.IntegerField(blank=True, help_text='Age of the athlete', null=True, verbose_name='Athlete age')),
                ('height', models.IntegerField(blank=True, help_text='Height of the athlete', null=True, verbose_name='Athlete height')),
                ('weight', models.IntegerField(blank=True, help_text='Weight of the athlete', null=True, verbose_name='Athlete weight')),
                ('noc', models.ForeignKey(help_text='National Olympic Committee 3 letter code', on_delete=django.db.models.deletion.CASCADE, to='Athlete.NOC', verbose_name='National Olympic Committee')),
            ],
        ),
    ]
