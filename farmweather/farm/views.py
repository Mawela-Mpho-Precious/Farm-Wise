from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import LocationForm
from .services import fetch_current_weather, fetch_forecast, summarize_5day
from .crops import suggest_crops
import requests
from datetime import datetime
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.views.decorators.http import require_http_methods

def group_daily_forecast(forecast):
    """Group forecast list (3-hourly data) into daily min/max + icon."""
    days = {}
    for entry in forecast.get("list", []):
        dt = datetime.fromtimestamp(entry["dt"])  # FIXED here
        date = dt.date()

        temp = entry["main"]["temp"]
        weather = entry["weather"][0]

        if date not in days:
            days[date] = {
                "date": date,
                "min": temp,
                "max": temp,
                "icon": weather["icon"],
                "condition": weather["main"]
            }
        else:
            days[date]["min"] = min(days[date]["min"], temp)
            days[date]["max"] = max(days[date]["max"], temp)

    return list(days.values())


def home(request):

    form = LocationForm(request.POST or None)
    context = {"form": form, "weather": None, "summary": None, "crops": [], "daily": []}

    if request.method == "POST" and form.is_valid():
        loc = form.cleaned_data["location"].strip()
        try:
            current = fetch_current_weather(loc)
            forecast = fetch_forecast(loc)
            summary = summarize_5day(forecast)
            daily = group_daily_forecast(forecast)[:6]  # next 6 days

            crops = suggest_crops(
                avg_temp=summary["avg_temp"] if summary else None,
                total_rain_mm=summary["total_rain_mm"] if summary else None
            )

            context.update({
                "weather": current,
                "summary": summary,
                "crops": crops,
                "daily": daily,
                "location_label": f'{current.get("name", loc)}, {current.get("sys", {}).get("country","")}'.strip(", "),
            })
        except requests.HTTPError as e:
            if e.response.status_code == 404:
                messages.error(request, "Location not found. Try another city or a city ID (e.g., 990930).")
            else:
                messages.error(request, f"Weather service error: {e.response.status_code}")
        except Exception as e:
            messages.error(request, f"Unexpected error: {e}")

    return render(request, "farm/home.html", context)

from django.shortcuts import render

def check_box(request):
    return render(request, "farm/click.html")  # your checkbox page

def login_page(request):
    return render(request, "farm/login.html")  # login page







@require_http_methods(["GET", "POST"])
@csrf_exempt
def login_view(request):
    # If user is already authenticated, redirect to home
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'GET':
        # Render the login page for GET requests
        return render(request, 'auth.html')
    
    elif request.method == 'POST':
        # Handle login for POST requests
        try:
            data = json.loads(request.body) if request.body else {}
            email = data.get('email', '')
            password = data.get('password', '')
            
            # Authenticate user
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                return JsonResponse({'success': True, 'message': 'Login successful', 'redirect': '/home/'})
            else:
                return JsonResponse({'success': False, 'message': 'Invalid email or password'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Error: {str(e)}'})

@require_http_methods(["POST"])
@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body) if request.body else {}
            full_name = data.get('full_name', '')
            email = data.get('email', '')
            password = data.get('password', '')
            confirm_password = data.get('confirm_password', '')
            
            # Check if passwords match
            if password != confirm_password:
                return JsonResponse({'success': False, 'message': 'Passwords do not match'})
            
            # Check if user already exists
            if User.objects.filter(email=email).exists():
                return JsonResponse({'success': False, 'message': 'User with this email already exists'})
            
            # Create new user
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = full_name
            user.save()
            
            # Log the user in
            login(request, user)
            
            return JsonResponse({'success': True, 'message': 'Account created successfully', 'redirect': '/home/'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Error creating account: {str(e)}'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@require_http_methods(["GET"])
def check_auth_view(request):
    if request.user.is_authenticated:
        return JsonResponse({'authenticated': True})
    else:
        return JsonResponse({'authenticated': False})

@require_http_methods(["GET"])
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Your home page logic here
    return render(request, 'farm/home.html')

@require_http_methods(["GET"])
def auth_page_view(request):
    # Render the authentication page
    return render(request, 'auth.html')

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')


def check_box(request):
    return render(request, "farm/click.html")  # your checkbox page

def home_page(request):
    return render(request,"home_page.html")

def journal(request):
   
    return render(request,'farm/journal.html')

def chat_page(request):
    return render(request, 'chatbot.html')

from datetime import datetime, timedelta
import random

def weather_dashboard(request):
    """
    View for the weather dashboard with chart data
    """
    # Simulate data for the last 7 days
    dates = [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(6, -1, -1)]
    temperatures = [random.randint(15, 35) for _ in range(7)]
    
    # Test performance data
    test_categories = ['Weather Alerts', 'Date Calculations', 'Pest Search']
    test_pass_rate = [100, 100, 100]
    
    # NEW: Pest distribution data for the pie chart
    pest_distribution = [45, 25, 20, 10]  # Aphids, Hornworms, Mildew, Other
    
    context = {
        'dates': dates,
        'temperatures': temperatures,
        'test_categories': test_categories,
        'test_pass_rate': test_pass_rate,
        'pest_distribution': pest_distribution,  # NEW: Add this line
    }
    return render(request, 'weather_dashboard.html', context)
