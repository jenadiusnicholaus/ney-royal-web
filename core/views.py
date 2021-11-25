
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator


from core.models import Applications, AppliedCourse, Course

# Create your views here.


def home(request):
    courses = Course.objects.all()
    context = {
        'courses': courses

    }
    return render(request, 'homepage.html', context=context)


def course(request):
    courses = Course.objects.all()
    paginator = Paginator(courses, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'courses': page_obj

    }
    return render(request, 'course.html', context=context)


def about_us(request):
    context = {

    }
    return render(request, 'about_us.html', context=context)


def contact_us(request):
    context = {

    }
    return render(request, 'contact_us.html', context=context)


def events(request):
    context = {

    }
    return render(request, 'events.html', context=context)


def course_details(request):
    context = {

    }
    return render(request, 'course_details.html', context=context)


def event_details(request):
    context = {

    }
    return render(request, 'event_details.html', context=context)


def appy_course(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        print(course_id)

        course = Course.objects.get(pk=course_id)
        applied_course, created = AppliedCourse.objects.get_or_create(
            student=request.user, course=course)
        application_qs = Applications.objects.filter(
            student=request.user)
        if application_qs.exists():
            application = application_qs[0]
            if application.courses.filter(course__pk=course.pk).exists():
                applied_course.save()
                messages.success(
                    request, f'You alread applied for this {course.title}')
                return redirect('/')
            else:
                application.courses.add(applied_course)
                messages.success(request, 'applacation added successifully')
                return redirect('/')
        else:
            application = Applications.objects.create(
                student=request.user, )
            application.courses.add(applied_course)
            messages.success(request, 'applacation added successifully')

            return redirect('/')
        return redirect('/')
