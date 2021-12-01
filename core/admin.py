from django.contrib import admin

from core.models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(AppliedCourse)
admin.site.register(Applications)
admin.site.register(Events)
admin.site.register(Messages)
