# Generated by Django 3.1.7 on 2021-03-13 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='registrations',
            field=models.ManyToManyField(blank=True, through='database.Registration', to='database.Section'),
        ),
    ]
