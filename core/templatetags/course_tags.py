from django import template
from core.models import *

register = template.Library()


@register.simple_tag
def isApplied(course_id, user):
    if user.is_authenticated:
        if AppliedCourse.objects.filter(course__pk=course_id, student=user).exists():
            return True
        else:
            return False
    else:

        return None
