from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


class Person(models.Model):
    email = models.CharField(max_length=124)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email_secondary = models.CharField(max_length=256)
    phone_primary = models.CharField(max_length=64)

    def __str__(self):
        return self.last_name + ', ' + self.first_name


class Role(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class CMPUser(User):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' <' + self.email + '>'


class Employer(models.Model):
    admin_user = models.ForeignKey(CMPUser, on_delete=models.CASCADE, null=True)
    website = models.CharField(max_length=1024)
    contact_person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.contact_person.first_name + ' ' + self.contact_person.last_name + ' (' + \
            self.contact_person.email + ')'


class Job(models.Model):
    title = models.CharField(max_length=1024, default=("Still to come " + str(timezone.now())), null=False)
    description = models.TextField(default="Still to come", null=models.NOT_PROVIDED)
    start_date = models.DateField(verbose_name='Start date')
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, null=models.NOT_PROVIDED)
    job_specific_contact = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title + ' starts ' + str(self.start_date)


class Question(models.Model):
    job = models.ManyToManyField(Job)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    choice_test = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_test
