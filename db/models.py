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
    """Тип курса - базовый, продолженный, DSN, Сахадж и т.д."""
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return '%d %s' % (self.id, self.name)

class Course(models.Model):
    start_date = models.DateField()
    end_date = models.DateField() # null = True
    city = models.ForeignKey(City)
    type = models.ForeignKey(CourseType)
    
    def __unicode__(self):
        return '%d %s %s %s' % (self.id, self.start_date, self.city.name, self.type.name)

class PersonStatus(models.Model):
    """'Статус' человека - учитель баз. курса, учитель YES и т.д., DSN, TTC1"""
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
    # info (PersonInfo)
   

    def __unicode__(self):
        return '%d %s %s %s %s' % (self.id, self.gender, self.first_name, self.last_name, self.birthday)

class PersonInfoType(models.Model):
    """Тип персональной информации (email, телефон, адрес, профессия и т.д.)"""
    name = models.CharField(max_length=50)
    #code = models.CharField(max_length=15)

    def __unicode__(self):
        return '%d %s' % (self.id, self.name)

class PersonInfo(models.Model):
    """Персональная информация"""
    person = models.ForeignKey(Person, related_name='info')
    type = models.ForeignKey(PersonInfoType)
    value = models.CharField(max_length=250)

    def __unicode__(self):
        return '%s %s' % (self.type.name, self.value)

class ParticipantType(models.Model):
    """Кем был на курсе - учитель, ассистент, участник"""
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return '%d %s' % (self.id, self.name)

class PersonsCources(models.Model):
    person = models.ForeignKey(Person)
    course = models.ForeignKey(Course)
    type = models.ForeignKey(ParticipantType)

    def __unicode__(self):
        return '%s %s %s %s' % (self.person.first_name, self.person.last_name, self.type.name, self.course.start_date)

    class Meta:
        db_table = 'db_person_cources'


