from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("", views.task_list, name="task_list"),
    path("tasks/create/", views.task_create, name="task_create"),
    path("tasks/<int:task_id>/edit/", views.task_update, name="task_update"),
    path("tasks/<int:task_id>/delete/", views.task_delete, name="task_delete"),
    path("tasks/<int:task_id>/complete/", views.task_complete, name="task_complete"),
]
