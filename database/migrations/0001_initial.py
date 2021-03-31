# Generated by Django 3.1.7 on 2021-03-31 21:32

import database.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('number', models.IntegerField()),
                ('credit_hours', models.IntegerField(default=4)),
                ('comments', models.TextField()),
                ('offered_annually', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModelSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PreferenceForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_taking_responses', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('set', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preference_form', to='database.modelset')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256)),
                ('year', models.IntegerField()),
                ('season', models.CharField(choices=[('FL', 'Fall'), ('WI', 'Winter'), ('SP', 'Spring'), ('SU', 'Summer')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WeekdaySet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.BooleanField(default=False)),
                ('tuesday', models.BooleanField(default=False)),
                ('wednesday', models.BooleanField(default=False)),
                ('thursday', models.BooleanField(default=False)),
                ('friday', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'possible weekdays',
            },
        ),
        migrations.CreateModel(
            name='Timeblock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_id', models.CharField(max_length=32, unique=True)),
                ('start_hour', models.IntegerField(choices=[(0, '00'), (1, '01'), (2, '02'), (3, '03'), (4, '04'), (5, '05'), (6, '06'), (7, '07'), (8, '08'), (9, '09'), (10, '10'), (11, '11'), (12, '12')])),
                ('start_minutes', models.IntegerField(choices=[(0, '00'), (5, '05'), (10, '10'), (15, '15'), (20, '20'), (25, '25'), (30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55')])),
                ('end_hour', models.IntegerField(choices=[(0, '00'), (1, '01'), (2, '02'), (3, '03'), (4, '04'), (5, '05'), (6, '06'), (7, '07'), (8, '08'), (9, '09'), (10, '10'), (11, '11'), (12, '12')])),
                ('end_minutes', models.IntegerField(choices=[(0, '00'), (5, '05'), (10, '10'), (15, '15'), (20, '20'), (25, '25'), (30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55')])),
                ('weekdays', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeblocks+', to='database.weekdayset')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(unique=True, validators=[database.validators.student_id_validator])),
                ('class_standing', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SetMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.modelset')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_id', models.CharField(max_length=4)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections+', to='database.course')),
                ('other_instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sections assisted with+', to='database.teacher')),
                ('primary_instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections taught+', to='database.teacher')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections+', to='database.schedule')),
                ('timeblock', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sections+', to='database.timeblock')),
            ],
        ),
        migrations.CreateModel(
            name='PreferenceFormEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100, verbose_name='Student Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Student Email')),
                ('courses', models.ManyToManyField(to='database.Course')),
                ('preference_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='database.preferenceform')),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.BooleanField()),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.course')),
                ('other_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other course+', to='database.course')),
                ('timeblock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.timeblock')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'preferences',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses offered+', to='database.department'),
        ),
    ]
