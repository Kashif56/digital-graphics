from django.shortcuts import redirect, render
from django.utils import timezone
from .models import course, teachers, message

# Create your views here.

today = timezone.now()


def home(request):
    teacher = teachers.objects.all()

    context = {
        'teachers': teacher
    }
    return render(request, 'index.html', context)


def courses(request):
    all_courses = course.objects.filter(is_activated=True, last_date__gt=today)

    context = {
        'courses': all_courses,
    }
    return render(request, 'courses.html', context)


def single_course(request, slug):
    get_course = course.objects.get(slug=slug)

    context = {
        'course': get_course,
    }
    return render(request, 'single_course.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')

        new_message = message(
            name=name,
            email=email,
            msg=msg
        )
        new_message.save()

        return redirect('core:index')
