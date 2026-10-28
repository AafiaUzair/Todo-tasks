To-Do Task Manager (Django)

Setup:
1) Install Django (one time):
   pip install django

2) Run migrations:
   python manage.py migrate

3) Create a superuser (admin login):
   python manage.py createsuperuser

4) Start the server:
   python manage.py runserver

Open:
http://127.0.0.1:8000/

Notes:
- Sign up page: /register/
- Login page: /accounts/login/
- Admin: /admin/
- Reminder time is set per task (15 minutes to 10 days).
