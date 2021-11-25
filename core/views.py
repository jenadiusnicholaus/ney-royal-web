from django.shortcuts import render
from django.core.paginator import Paginator


from core.models import Course

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
