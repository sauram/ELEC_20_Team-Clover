# Generated by Django 3.0.2 on 2020-02-02 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.FloatField(default=0.0)),
                ('b', models.FloatField(default=0.0)),
                ('c', models.FloatField(default=0.0)),
                ('d', models.FloatField(default=0.0)),
                ('e', models.FloatField(default=0.0)),
                ('f', models.FloatField(default=0.0)),
                ('g', models.FloatField(default=0.0)),
                ('h', models.FloatField(default=0.0)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('today', models.DateField()),
                ('time', models.TimeField()),
                ('area', models.FloatField(default=0.0)),
                ('fire', models.IntegerField(default=0)),
            ],
        ),
    ]