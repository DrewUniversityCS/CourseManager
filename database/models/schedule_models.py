from django.db import models

from database.reliability.enums import SEASONS, POSSIBLE_HOURS, POSSIBLE_MINUTES, WEEKDAYS


class Course(models.Model):
    department = models.ForeignKey("database.Department", on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=False, null=False)
    number = models.IntegerField(blank=False, null=False)
    CRN = models.IntegerField(blank=False, null=False)
    max_enrollment = models.IntegerField(blank=False, null=True)
    cross_listed_with = models.ManyToManyField("database.Course", related_name="cross listed with")
    prereqs = models.ManyToManyField("database.Course", related_name="prerequirement_for")
    coreqs = models.ManyToManyField("database.Course", related_name="corequirement_for")
    credit_hours = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return self.department.abbreviation + str(self.number)


class Section(models.Model):
    course = models.ForeignKey("database.Course", on_delete=models.CASCADE)
    section_id = models.CharField(max_length=4, blank=False, null=False)
    primary_instructor = models.ForeignKey("database.Teacher", on_delete=models.CASCADE,
                                           related_name="primary instructor")
    other_instructor = models.ForeignKey("database.Teacher", on_delete=models.CASCADE,
                                         related_name="secondary instructor")
    room = models.ForeignKey("database.Room", on_delete=models.CASCADE)
    year = models.IntegerField(blank=False, null=False)
    season = models.CharField(choices=SEASONS, max_length=50)
    timeblock = models.ForeignKey("database.TimeBlock", on_delete=models.CASCADE)

    def __str__(self):
        return self.course.name + " " + self.course.department.abbreviation + "-" + str(self.course.number)\
               + " Section " + self.section_id


class Schedule(models.Model):
    name = models.CharField(max_length=256, blank=True)
    monday = models.ForeignKey("database.Weekday", related_name="monday", on_delete=models.CASCADE)
    tuesday = models.ForeignKey("database.Weekday", related_name="tuesday", on_delete=models.CASCADE)
    wednesday = models.ForeignKey("database.Weekday", related_name="wednesday", on_delete=models.CASCADE)
    thursday = models.ForeignKey("database.Weekday", related_name="thursday", on_delete=models.CASCADE)
    friday = models.ForeignKey("database.Weekday", related_name="friday", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Weekday(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False, choices=WEEKDAYS)

    def __str__(self):
        return self.name


class TimeBlock(models.Model):
    weekday = models.ForeignKey("database.Weekday", on_delete=models.CASCADE)
    start_hour = models.IntegerField(choices=POSSIBLE_HOURS)
    start_minutes = models.IntegerField(choices=POSSIBLE_MINUTES)
    end_hour = models.IntegerField(choices=POSSIBLE_HOURS)
    end_minutes = models.IntegerField(choices=POSSIBLE_MINUTES)

    def __str__(self):
        return self.weekday.name + str(self.start_hour) + ":" + str(self.start_minutes)
