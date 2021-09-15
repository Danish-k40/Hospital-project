
from django.shortcuts import render, redirect, get_object_or_404
from .models import doctor, cato
from django.http import HttpResponse
from news.models import news
# Create your views here.
from appointment.models import Appointment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.db.models import Q

def fun(request):
    obj = doctor.objects.all()
    n = news.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        health = request.POST.get('health')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        if name == "" or phone == "":
            messages.info(request, "fill the details")
        else:
            obj1 = Appointment(name=name, email=email, date=date, health=health, phone=phone, msg=msg)
            obj1.save()
    cat = cato.objects.all()
    return render(request, 'index.html', {'results': obj, 'c': cat, 'ci':n})

def readmore(request):

    o = news.objects.all()
    c = cato.objects.all()
    return render(request, 'blog.html', { 'cat': c, 'r':o})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def doctors(request):
    o = doctor.objects.all()
    return render(request, 'doctors.html', {'res': o})


def doctor_details(request, c_slug, doctor_slug):
    # doctor1 = doctor.objects.get(id=id)
    try:
        det = doctor.objects.get(category__slug=c_slug, slug=doctor_slug)
    except Exception as e:
        raise e

    return render(request, 'blog-details.html', {'details': det})


def search(request):
    do = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        do = doctor.objects.all().filter(Q(name__contains=query) | Q(dept__contains=query))
    return render(request, 'search.html', {'qr':query, 'dr':do})

