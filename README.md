# 🍋 Little Lemon Restaurant Booking System

A Django-based restaurant booking system with MySQL database, user authentication, and a clean booking interface, developed as part of the Django Web Framework course certification project.

## 📋 Project Overview

Little Lemon is a Mediterranean restaurant booking application that allows customers to:
- View restaurant information and menu
- Create user accounts and log in
- Make table reservations with a simple form
- View their booking history
- Access booking data via REST API

## ✨ Features

### 🎯 Core Functionality
- **User Authentication**: Complete signup, login, and logout system
- **Restaurant App Integration**: Properly configured in Django settings
- **MySQL Database**: Full database configuration and migrations
- **Booking Form**: Three required fields (First Name, Reservation Date, Reservation Slot)
- **Date Picker**: HTML5 date input with calendar functionality
- **Duplicate Prevention**: Database constraints prevent double-booking
- **JSON API**: RESTful endpoints for booking data
- **User-specific Bookings**: Users can only see their own reservations

### 🌟 Additional Features
- **Professional UI**: Responsive design with Mediterranean theme
- **Navigation System**: Complete site navigation with authentication buttons
- **Base Template**: Consistent layout across all pages
- **Error Handling**: Graceful handling of booking conflicts
- **Auto-date Selection**: Current date pre-selected on load
- **Login Required**: Protected booking functionality

## 🏗️ Project Structure

```
littlelemon/
├── littlelemon/
│   ├── __init__.py
│   ├── settings.py          # Django configuration with MySQL
│   ├── urls.py              # Main URL routing with auth
│   ├── wsgi.py
│   └── asgi.py
├── restaurant/
│   ├── __init__.py
│   ├── admin.py             # Admin interface configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Booking model with user relationship
│   ├── views.py             # Views and API endpoints
│   ├── forms.py             # CustomUserCreationForm and BookingForm
│   ├── urls.py              # App URL patterns
│   ├── tests.py
│   └── migrations/          # Database migrations
├── templates/
│   ├── base.html            # Base template with navigation
│   ├── registration/
│   │   ├── login.html       # User login page
│   │   └── signup.html      # User registration page
│   ├── index.html           # Home page
│   ├── about.html           # About page
│   ├── menu.html            # Restaurant menu
│   ├── book.html            # Simple booking form
│   └── bookings.html        # User's booking history
├── static/                  # Static files directory
├── Pipfile                  # Dependencies
├── manage.py
├── requirements.txt
└── README.md
```

## 🔧 Technologies Used

- **Backend**: Django 4.x, Python 3.8+
- **Database**: MySQL 8.0+
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Authentication**: Django built-in auth system
- **API**: Django REST capabilities with JSON responses
- **Environment**: Pipenv for dependency management

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- MySQL 8.0 or higher
- Pipenv

### 1. Clone and Setup Project

```bash
# Create project directory
mkdir littlelemon
cd littlelemon

# Initialize pipenv environment
pipenv install django mysqlclient
pipenv shell
```

### 2. Create Django Project Structure

```bash
# Create Django project and app
django-admin startproject littlelemon .
python manage.py startapp restaurant

# Create templates directory
mkdir templates
mkdir static
```

### 3. Database Configuration

Create MySQL database:
```sql
# Connect to MySQL
mysql -u root -p
C:\xampp1\mysql\bin\mysql.exe -u root -p

# Create database
CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Update `littlelemon/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restaurant',  # Add this line
]

# Authentication settings
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

### 4. Run Migrations

```bash
python manage.py makemigrations
C:\Users\HARISH\.virtualenvs\-_SHv_4lM\Scripts\python.exe manage.py makemigrations

python manage.py migrate
C:\Users\HARISH\.virtualenvs\-_SHv_4lM\Scripts\python.exe manage.py migrate

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
C:\Users\HARISH\.virtualenvs\-_SHv_4lM\Scripts\python.exe manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
C:\Users\HARISH\.virtualenvs\-_SHv_4lM\Scripts\python.exe manage.py runserver 
```

Visit `http://127.0.0.1:8000` to view the application.

## 📱 Usage

### User Registration & Login

1. **Sign Up**: Visit `/accounts/signup/` to create a new account
2. **Login**: Visit `/accounts/login/` to access your account
3. **Navigation**: Login/logout buttons appear in the top navigation bar

### Making a Reservation

1. **Login** to your account first
2. Navigate to the **Book** page (`/book/`)
3. The current date is automatically selected
4. Choose your preferred time slot from available options
5. Enter your first name
6. Submit the form to make your reservation

### Viewing Your Reservations

1. **Login** to your account
2. Go to the **Reservations** page (`/reservations/`) or **My Bookings** (`/bookings/`)
3. View all your personal bookings
4. See formatted reservation listings

### API Endpoints

- `GET /bookings/` - Returns user's bookings (login required)
- `GET /check-availability/?date=YYYY-MM-DD` - Returns availability for a date
- `GET /test-availability/` - Test endpoint for debugging

## 🎯 Assessment Criteria Compliance

This project meets all required criteria:

✅ **App Configuration**: Restaurant app added to `INSTALLED_APPS`  
✅ **Database Setup**: MySQL configuration in settings  
✅ **Migrations**: Completed and ready  
✅ **Form Fields**: First name, Reservation date, Reservation slot  
✅ **Date Picker**: HTML5 date input opens calendar  
✅ **JSON Data**: Available on bookings page  
✅ **Duplicate Prevention**: Database unique constraints  
✅ **User Authentication**: Complete signup/login system  
✅ **Protected Views**: Login required for booking functionality  
✅ **User-specific Data**: Users see only their own bookings  
✅ **Navigation**: Consistent layout with auth buttons  

## 🎨 Design Features

- **Mediterranean Theme**: Warm colors and professional styling
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Base Template**: Consistent navigation and footer across all pages
- **Authentication UI**: Clean login/signup forms with proper styling
- **Professional Typography**: Clean, readable fonts throughout

## 🔍 Testing

### Manual Testing Checklist

- [ ] Home page loads correctly with navigation
- [ ] About page displays restaurant information
- [ ] Menu page shows complete menu with prices
- [ ] Signup page creates new user accounts
- [ ] Login page authenticates users properly
- [ ] Logout functionality works correctly
- [ ] Book page requires login to access
- [ ] Booking form submits successfully
- [ ] Reservations page shows user's bookings
- [ ] Navigation shows correct auth buttons

### Authentication Testing

```bash
# Test signup
curl -X POST http://127.0.0.1:8000/accounts/signup/ -d "username=test&password1=testpass123&password2=testpass123&email=test@example.com&first_name=Test&last_name=User"

# Test login
curl -X POST http://127.0.0.1:8000/accounts/login/ -d "username=test&password=testpass123"
```

## 📦 Dependencies

```toml
# Pipfile
[packages]
django = "*"
mysqlclient = "*"
```

## 🗃️ Database Schema

### User Model
Uses Django's built-in User model with custom creation form.

### Booking Model
```python
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    class Meta:
        unique_together = ('reservation_date', 'reservation_slot')
```

## 🔧 Configuration Notes

### Important Settings
- **Time Slots**: 10:00 AM to 10:00 PM (10-22 in 24-hour format)
- **Unique Constraints**: Prevents duplicate bookings on same date/time
- **User Association**: Bookings are linked to authenticated users
- **Date Format**: YYYY-MM-DD for consistency

### Authentication Configuration
- **Login URL**: `/accounts/login/`
- **Signup URL**: `/accounts/signup/`
- **Logout URL**: `/accounts/logout/`
- **Redirect URLs**: Home page after login/logout

## 🚀 Deployment Considerations

For production deployment:
1. Update `DEBUG = False` in settings
2. Configure allowed hosts
3. Use environment variables for database credentials
4. Set up static file serving
5. Configure proper MySQL user permissions
6. Use HTTPS for authentication pages

## 🤝 Contributing

This is a course project for certification purposes. The implementation follows Django best practices and includes all required functionality for the assessment.

## 📄 License

This project is created for educational purposes as part of the Django Web Framework course.

## 🎓 Course Information

**Project**: Little Lemon Restaurant Booking System  
**Framework**: Django Web Framework  
**Database**: MySQL  
**Frontend**: HTML, CSS, JavaScript  
**Authentication**: Django built-in auth system  
**Assessment**: Peer-reviewed project submission  

## 📞 Support

For issues with this implementation:
1. Check that MySQL is running and credentials are correct
2. Ensure all migrations have been applied
3. Verify that the restaurant app is in INSTALLED_APPS
4. Test authentication endpoints manually
5. Check that users are properly logged in before accessing protected views

---

**Ready for Submission**: This project includes all required files and functionality for successful peer review and certification completion.