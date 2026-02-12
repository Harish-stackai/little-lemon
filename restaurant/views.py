from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
from .forms import CustomUserCreationForm, BookingForm
from .models import Booking

# Your existing home view (no changes needed)
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

# ADD new view for checking availability (no login required)
def check_availability(request):
    """View for checking available time slots for a specific date - no login required"""
    date_str = request.GET.get('date')
    if not date_str:
        return JsonResponse({'error': 'Date parameter required'}, status=400)
    
    try:
        qs = Booking.objects.filter(reservation_date=date_str).order_by('reservation_slot')
        data = [
            {
                'first_name': b.first_name,
                'reservation_date': b.reservation_date.strftime('%Y-%m-%d'),
                'reservation_slot': b.reservation_slot,
            }
            for b in qs
        ]
        print(f"Availability check for {date_str}: {len(data)} bookings found")
        return JsonResponse(data, safe=False)
    except Exception as e:
        print(f"Error in availability check: {e}")
        return JsonResponse({'error': str(e)}, status=500)

# Simple test view to check if the endpoint is working
def test_availability(request):
    """Simple test view to check if the availability endpoint is working"""
    try:
        # Get today's date
        from datetime import date
        today = date.today().strftime('%Y-%m-%d')
        
        # Check if there are any bookings at all
        total_bookings = Booking.objects.count()
        
        # Check today's bookings
        today_bookings = Booking.objects.filter(reservation_date=today).count()
        
        return JsonResponse({
            'message': 'Availability endpoint is working',
            'total_bookings': total_bookings,
            'today_bookings': today_bookings,
            'today_date': today
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# MODIFY your book view to require login and associate with user
@login_required
def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Associate booking with logged-in user
            try:
                booking.save()
                messages.success(request, 'Booking confirmed successfully!')
                return redirect('bookings')  # Redirect to user's bookings
            except:
                messages.error(request, 'This time slot is already booked. Please choose another time.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookingForm()
    
    return render(request, 'book.html', {'form': form})

# ADD new view for user's bookings
@login_required
def bookings(request):
    # Check if this is an AJAX/API request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
        # Return JSON data for all bookings (not just user's)
        all_bookings = Booking.objects.all().order_by('reservation_date', 'reservation_slot')
        data = [
            {
                'first_name': b.first_name,
                'reservation_date': b.reservation_date.strftime('%Y-%m-%d'),
                'reservation_slot': b.reservation_slot,
                'user': b.user.username if b.user else 'Anonymous'
            }
            for b in all_bookings
        ]
        return JsonResponse(data, safe=False)
    
    # If a specific date is requested, return JSON for frontend to show availability
    date_str = request.GET.get('date')
    if date_str:
        qs = Booking.objects.filter(reservation_date=date_str).order_by('reservation_slot')
        data = [
            {
                'first_name': b.first_name,
                'reservation_date': b.reservation_date.strftime('%Y-%m-%d'),
                'reservation_slot': b.reservation_slot,
            }
            for b in qs
        ]
        return JsonResponse(data, safe=False)

    user_bookings = Booking.objects.filter(user=request.user).order_by('-reservation_date', '-reservation_slot')
    return render(request, 'bookings.html', {'bookings': user_bookings})

# ADD signup view
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Account created successfully! Please log in.')
        return response