from typing import Reversible
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Course(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.FileField(upload_to='course_files', null=False)
    title = models.CharField(max_length=300, null=True)
    slug = models.SlugField(max_length=400, null=False)
    description = models.TextField(null=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return Reversible("course_detail", kwargs={"pk": self.pk})


class AppliedCourse(models.Model):
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(
        Course, on_delete=models.SET_NULL, null=True)
    is_applied = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Applied course"
        verbose_name_plural = "Applied courses"

    def __str__(self):
        return self.course.title

    def get_absolute_url(self):
        return Reversible("course_detail", kwargs={"pk": self.course.pk})


class Applications(models.Model):
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    courses = models.ManyToManyField(AppliedCourse)
    file = models.FileField(upload_to='application_files', null=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "applications"
        verbose_name_plural = "Applicants"

    def __str__(self):
        return self.student.username

    def get_absolute_url(self):
        return Reversible("course_detail", kwargs={"pk": self.course.pk})


class Events(models.Model):
    organisors = models.ManyToManyField(User)
    image = models.FileField(upload_to='Event_files',)
    title = models.CharField(max_length=1000, null=True)
    description = models.TextField(null=True)
    held_on = models.DateTimeField(null=True)
    address = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = "Events"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title


class Messages(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=200, null=True)
    message = models.TextField(null=True)

    class Meta:
        verbose_name = "Messagess"
        verbose_name_plural = "Messages"

    def __str__(self):
        return self.name
