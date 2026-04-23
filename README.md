# EduTrack Pro

EduTrack Pro is a Django-based Student Management System designed to manage students, subjects, attendance, reports, and enrollments from a unified interface.

## Project Overview

- Django project with modular apps inside the `apps/` directory.
- Apps: `accounts`, `students`, `subjects`, `attendance`, `reports`, `enrollments`.
- Uses Django ORM with MySQL database configuration.
- Templates stored in a global `templates/` directory.
- Static assets served from `static/css/style.css`.

## Project Structure

```
edutrack_pro/
├── export_project.txt
├── project_extraction.txt
├── README.md
├── manage.py
├── edutrack_pro/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── accounts/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── migrations/
│   │       ├── __init__.py
│   │       └── 0001_initial.py
│   ├── students/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── migrations/
│   │       ├── __init__.py
│   │       └── 0001_initial.py
│   ├── attendance/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── migrations/
│   │       ├── __init__.py
│   │       └── 0001_initial.py
│   ├── subjects/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── migrations/
│   │       ├── __init__.py
│   │       └── 0001_initial.py
│   ├── reports/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── enrollments/
│       └── admin.py
├── static/
│   └── css/
│       └── style.css
└── templates/
    ├── base.html
    ├── dashboard.html
    ├── accounts/
    │   └── login.html
    ├── attendance/
    │   ├── list.html
    │   └── mark.html
    ├── reports/
    │   └── report.html
    ├── students/
    │   ├── add.html
    │   ├── delete.html
    │   ├── edit.html
    │   └── list.html
    └── subjects/
        ├── add.html
        └── list.html
```

## Implemented Features

- Student CRUD (Create, Read, Update, Delete)
- Subject CRUD
- Attendance tracking by student, subject, date, and status
- Attendance reports with summary percentages
- Enrollment management
- Authentication system with role-based users (`admin`, `teacher`)
- All protected views using `@login_required`
- Professional dashboard and UI updates

## Dashboard Features

- Total number of students
- Total number of subjects
- Total number of attendance records
- Modern card-based layout with consistent design
- Dashboard route included in main `urls.py`
- Dashboard link available in navbar

## Setup Instructions

1. Open a terminal and go to the project folder:
   ```powershell
   cd c:\Users\admin\OneDrive\Documents\Desktop\SMS\edutrack_pro
   ```

2. Activate your Conda environment:
   ```powershell
   conda activate django_learning
   ```

3. Install Django if needed:
   ```powershell
   pip install django
   ```

4. Run migrations:
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```powershell
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```powershell
   python manage.py runserver
   ```

7. Open the app in your browser:
   - Main app: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Notes on Configuration

- `settings.py` uses MySQL with credentials set in the `DATABASES` section.
- Static files are loaded from `static/css/style.css` using `{% load static %}` in templates.
- Global templates are stored in `templates/` with app-specific subfolders.
- App configs use `name = 'apps.<app_name>'` for correct project import paths.

## App Descriptions

- `accounts`: login/logout, dashboard view, user roles.
- `students`: student list, add, edit, delete operations.
- `subjects`: subject list and creation.
- `attendance`: attendance record creation and listing.
- `reports`: attendance summary reports.
- `enrollments`: enrollment management.

## Frontend Design

- Dark navbar with modern accent colors
- White cards with shadows and hover effects
- Responsive grid layout for dashboard cards
- Consistent form and table styling across pages
- Clean semantic HTML structure

## Troubleshooting

- If Django cannot import `apps.<app_name>`, verify `apps.py` `name` settings and `INSTALLED_APPS`.
- If static files do not load, verify `STATIC_URL = '/static/'` in `settings.py`.
- If the project still does not start, run `python manage.py check` to identify configuration issues.

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make changes and test.
4. Submit a pull request.

## License

This project is created for learning and educational use. Feel free to modify and adapt it as needed.
=======
# sms-project
>>>>>>> 9c920ebca7da276b0423ccf5bb29522aefb0345f
