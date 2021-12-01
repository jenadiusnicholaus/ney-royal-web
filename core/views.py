
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
        if request.user.is_authenticated:
            user_form = usersForm(instance=request.user)
            user_profile_form = UserProfileForm(
                instance=request.user.userprofile)
            user_application = Applications.objects.filter(
                student=request.user)
            user_ap = None

            if user_application.exists():
                user_ap = user_application[0]

            context = {
                'application': user_ap,
                'user_appliction': user_application,
                'user_form': user_form,
                'profile_form': user_profile_form
            }
            return render(request, 'update_application.html', context=context)
        messages.warning(
            self.request, 'Login to continue')
        return redirect("/")

    def post(self, request, *kwargs, **kargs):

        user_form = usersForm(
            self.request.POST,
            instance=self.request.user)
        user_profile_form = UserProfileForm(
            self.request.POST or None, self.request.FILES or None,
            instance=self.request.user.userprofile)
        if user_form.is_valid() and user_profile_form.is_valid():

            user = user_form.save(True)
            profile = user_profile_form.save(False)
            profile.user = user
            profile.save()
            messages.success(
                self.request, 'your profile has been updated successfully')
            return redirect('update_application')
        else:
            messages.warning(self.request, 'form is invalid')

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


def course_details(request, pk):
    course = Course.objects.get(pk=pk)
    context = {
        'course': course
    }
    return render(request, 'course_details.html', context=context)


def event_details(request, pk):
    event = Events.objects.get(pk=pk)

    context = {
        'event': event

    }
    return render(request, 'event_details.html', context=context)


def contact_msg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('message')
        cont_msg = Messages(name=name, email=email, message=msg)
        cont_msg.save()
        messages.success(
            request, f'Thanks for reaching out')
        return redirect('contact_us')


def appy_course(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            course_id = request.POST.get('course_id')
            coverlatter = None
            if request.FILES.get('cover_letter') is not None:
                coverlatter = request.FILES.get('cover_letter')

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
                    messages.success(
                        request, 'application added successifully')
                    return redirect('/')
            else:
                application = Applications.objects.create(
                    student=request.user, )
                application.courses.add(applied_course)
                messages.success(request, 'application added successifully')

        return redirect('/')
    messages.warning(request, 'Login to continue')

    return redirect('/')
