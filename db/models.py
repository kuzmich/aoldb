# -*- coding: utf-8 -*-
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return '%d %s' % (self.id, self.name)

class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return '%d %s' % (self.id, self.name)

class CourseType(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return '%d %s' % (self.id, self.name)

class Course(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    city = models.ForeignKey(City)
    type = models.ForeignKey(CourseType)
    
class PersonStatus(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return '%d %s' % (self.id, self.name)

class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patr_name = models.CharField(max_length=50)
    birthday = models.DateField()
    city = models.ForeignKey(City)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    statuses = models.ManyToManyField(PersonStatus)
    cources = models.ManyToManyField(Course, through='PersonsCources')
   

    def __unicode__(self):
        return '%d %d %s' % (self.id, self.code, self.name)

class PersonInfoType(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return '%d %s' % (self.id, self.name)

class PersonInfo(models.Model):
    person = models.ForeignKey(Person)
    type = models.ForeignKey(PersonInfoType)
    text = models.CharField(max_length=250)

    def __unicode__(self):
        return '%d %s' % (self.id, self.name)

class ParticipantType(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return '%d %s' % (self.id, self.name)

class PersonsCources(models.Model):
    person = models.ForeignKey(Person)
    course = models.ForeignKey(Course)
    type = models.ForeignKey(ParticipantType)

    def __unicode__(self):
        return '%d %s' % (self.id, self.name)

    class Meta:
        db_table = 'db_person_cources'


