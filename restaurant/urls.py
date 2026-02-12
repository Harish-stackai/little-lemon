from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    path('bookings/', views.bookings, name='bookings'),  # ADD this new URL
    path('reservations/', views.bookings, name='reservations'),  # ADD reservations URL
    path('check-availability/', views.check_availability, name='check_availability'),  # ADD availability check URL
    path('test-availability/', views.test_availability, name='test_availability'),  # ADD test URL
]