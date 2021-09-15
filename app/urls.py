from django.urls import path
from . import views
urlpatterns = [
    path('', views.fun, name='fun'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('doctor', views.doctors, name='doctor'),
    path('readmore', views.readmore, name='readmore'),
    path('<slug:c_slug>/<slug:doctor_slug>', views.doctor_details, name='doctor_details'),
    path('search', views.search, name='search')
]
