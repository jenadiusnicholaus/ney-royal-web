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
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "applications"
        verbose_name_plural = "Applicants"

    def __str__(self):
        return self.student.username

    def get_absolute_url(self):
        return Reversible("course_detail", kwargs={"pk": self.course.pk})
