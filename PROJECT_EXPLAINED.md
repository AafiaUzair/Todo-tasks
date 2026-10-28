# To-Do Task Manager (Simple Explanation)

This project is a very basic Django website where people can create tasks, set due dates, and mark them as done. It is made to be simple for beginners.

## Big Picture (Easy Words)

- **Model** = what data exists (Task info).
- **View** = the Python logic (what happens when you click).
- **Template** = HTML pages (what you see in the browser).
- **URL** = the page address (where you go).

## What Each File Does

### `manage.py`
The main command file.
- You run this to start the server.
- You run this to create database tables.

### `todo_manager/settings.py`
Main settings for the whole project.
- Uses SQLite database.
- Password must be at least 7 characters.
- Time zone is set to **Asia/Karachi**.
- Tells Django where templates and static files are.

### `todo_manager/urls.py`
Main URL list.
- `/admin/` → admin page.
- `/accounts/` → login/logout pages.
- `/` → tasks app (main app).

### `tasks/models.py`
Defines the Task table (data):
- title, description, category, priority
- due date, completed flag, completed time
- reminder time in seconds (min 30s, max 10 days)

### `tasks/forms.py`
Form rules:
- Signup form (username, password, etc.)
- Task form (title, due date, reminder seconds)
- Category is a dropdown.

### `tasks/views.py`
Logic for pages:
- Register user
- List tasks (filter, search)
- Create/edit/delete tasks
- Mark task done
- Calculate "Time left"

### `tasks/urls.py`
Connects task pages:
- `/` list tasks
- `/register/` signup
- `/tasks/create/` add task
- `/tasks/<id>/edit/` edit
- `/tasks/<id>/delete/` delete
- `/tasks/<id>/complete/` mark done

### `tasks/admin.py`
Shows tasks in Django admin panel.

### `tasks/migrations/`
Database history (table changes).
- Django uses these to create/modify tables.

### Templates (`templates/`)
HTML pages:
- `base.html` layout (header and nav)
- `registration/login.html` login page
- `tasks/register.html` signup page
- `tasks/task_list.html` task list + popup + table
- `tasks/task_form.html` add/edit task page
- `tasks/task_confirm_delete.html` delete confirm page

### Static Files (`static/`)
- `styles.css` basic styling (colors, table, popup).

## How the Site Works (Simple Steps)

1) User signs up at `/register/`.
2) User logs in at `/accounts/login/`.
3) User creates tasks.
4) Tasks show in a table.
5) Clicking a task title shows a popup.
6) Marking done sets status to "Completed".
7) The page auto-refreshes to update status.

## Commands You Use

Install Django:
```
pip install django
```

Create tables:
```
python manage.py migrate
```

Create admin user:
```
python manage.py createsuperuser
```

Run server:
```
python manage.py runserver
```

Open site:
```
http://127.0.0.1:8000/
```
