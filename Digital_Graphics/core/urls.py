from django.urls import path

from . import views

app_name = 'core'


urlpatterns = [
    path('', views.home, name='index'),
    path('courses/', views.courses, name='courses'),
    path('course-detail/?=<slug:slug>/',
         views.single_course, name='course-detail'),

    path('send-message/', views.contact, name='send-message'),
]
