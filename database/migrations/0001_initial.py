# Generated by Django 3.1.6 on 2021-02-21 21:32

import database.reliability.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('name', models.CharField(max_length=256, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('number', models.IntegerField()),
                ('CRN', models.IntegerField()),
                ('max_enrollment', models.IntegerField(null=True)),
                ('credit_hours', models.IntegerField()),
                ('comments', models.TextField()),
                ('coreqs', models.ManyToManyField(related_name='_course_coreqs_+', to='database.Course')),
                ('cross_listed_with', models.ManyToManyField(related_name='_course_cross_listed_with_+', to='database.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('abbreviation', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=256, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('max_occupancy', models.IntegerField(null=True)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.building')),
            ],
        ),
        migrations.CreateModel(
            name='TimeBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overseeing_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(unique=True, validators=[database.reliability.validators.student_id_validator])),
                ('class_standing', models.CharField(choices=[('1', 'Freshman'), ('2', 'Sophomore'), ('3', 'Junior'), ('4', 'Senior'), ('5', 'Post Graduate')], max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_id', models.CharField(max_length=4)),
                ('year', models.IntegerField()),
                ('season', models.CharField(choices=[('1', 'Fall'), ('2', 'Winter'), ('3', 'Spring'), ('4', 'Summer')], max_length=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.course')),
                ('other_instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondary instructor +', to='database.teacher')),
                ('primary_instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary instructor +', to='database.teacher')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.room')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friday', to='database.weekday')),
                ('monday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monday', to='database.weekday')),
                ('thursday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thursday', to='database.weekday')),
                ('tuesday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tuesday', to='database.weekday')),
                ('wednesday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wednesday', to='database.weekday')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='department_head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.teacher'),
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.department'),
        ),
        migrations.AddField(
            model_name='course',
            name='prereqs',
            field=models.ManyToManyField(related_name='_course_prereqs_+', to='database.Course'),
        ),
    ]
