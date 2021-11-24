from django.shortcuts import render

# Create your views here.


def home(request):
    context = {

    }
    return render(request, 'homepage.html', context=context)


def course(request):
    context = {

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
