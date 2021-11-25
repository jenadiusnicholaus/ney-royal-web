from django.contrib import admin

from core.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Course, CourseAdmin)
