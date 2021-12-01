from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course/', views.course, name='course'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('events/', views.events, name='events'),
    path('course_details/<int:pk>', views.course_details, name='course_details'),
    path('event_details/<pk>', views.event_details, name='event_details'),
    path('appy_course', views.appy_course, name="appy_course"),
    path('update_application', views.UpdateAppliction.as_view(),
         name="update_application")


]
