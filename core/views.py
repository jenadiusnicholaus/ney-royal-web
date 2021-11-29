
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from authentication.forms import UserProfileForm, usersForm
from core.forms import ApllicationForm
from django.views.generic import View


from core.models import *
# Create your views here.


def home(request):
    events = Events.objects.all()[:2]
    form = ApllicationForm()
    if request.user.is_authenticated:
        application_qs = Applications.objects.filter(student=request.user)
        application = None
        if application_qs.exists():
            application = application_qs[0]

        print(application.courses.count())
        courses = Course.objects.all()
        context = {
            'courses': courses,
            'events': events,
            'application_form': form,
            'application_course_counter': application.courses.count()

        }
        return render(request, 'homepage.html', context=context)
    else:
        courses = Course.objects.all()
        context = {
            'courses': courses,
            'events': events,
            'application_form': form,
        }
        return render(request, 'homepage.html', context=context)


class UpdateAppliction(View):
    def get(self, request, *kwargs, **kargs):
        application_form = ApllicationForm(instance=request.user)
        update_form_user = usersForm(instance=request.user)
        update_form_user_profile = UserProfileForm(
            instance=request.user.userprofile)
        user_application = Applications.objects.filter(student=request.user)
        user_ap = None

        if user_application.exists():
            user_ap = user_application[0]

        context = {
            'application': user_ap,
            'a_form': application_form,
            'user_appliction': user_application,
            'user_form': update_form_user,
            'profile_form': update_form_user_profile
        }

        return render(request, 'update_application.html', context=context)

    def post(self, request, *kwargs, **kargs):

        update_form_user = usersForm(
            self.request.POST or None,
            instance=self.request.user)
        update_form_user_profile = UserProfileForm(
            self.request.POST or None, self.request.FILES or None,
            instance=self.request.user.userprofile)
        if update_form_user.is_valid() and update_form_user_profile.is_valid():

            user = update_form_user.save(True)
            profile = update_form_user_profile.save(False)
            profile.user = user
            profile.save()
            messages.success(
                self.request, 'your profile has been updated successfully')
            return redirect('update_application')
        else:
            messages.warning(self.request, 'form is invalid')
            print(update_form_user.data, update_form_user_profile.data)
            return redirect('update_application')


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
    events = Events.objects.all()
    paginator = Paginator(events, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'events': page_obj

    }
    return render(request, 'events.html', context=context)


def course_details(request):
    context = {

    }
    return render(request, 'course_details.html', context=context)


def event_details(request):
    events = Events.objects.all()
    paginator = Paginator(events, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'events': page_obj

    }
    return render(request, 'event_details.html', context=context)


def appy_course(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        coverlatter = request.FILES['cover_letter']
        print(course_id)
        print(coverlatter)

        course = Course.objects.get(pk=course_id)
        applied_course, created = AppliedCourse.objects.get_or_create(
            student=request.user, course=course)
        application_qs = Applications.objects.filter(
            student=request.user)
        if application_qs.exists():
            application = application_qs[0]
            if application.courses.filter(course__pk=course.pk).exists():
                applied_course.save()
                if application.file is None:
                    application.file = coverlatter
                    application.save()
                    messages.success(
                        request, f'You alread applied for this {course.title} course but added a file')
                    return redirect('/')
                messages.success(
                    request, f'You alread applied for this {course.title} course ')
                return redirect('/')
            else:
                application.courses.add(applied_course)
                messages.success(request, 'application added successifully')
                return redirect('/')
        else:
            application = Applications.objects.create(
                student=request.user, )
            application.courses.add(applied_course)
            messages.success(request, 'application added successifully')

            return redirect('/')
        return redirect('/')
