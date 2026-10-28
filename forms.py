from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Task


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class TaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        input_formats=["%Y-%m-%dT%H:%M"],
    )
    category = forms.ChoiceField(
        choices=[("", "Select category")] + Task.CATEGORY_CHOICES,
        required=False,
    )

    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "category",
            "priority",
            "due_date",
            "completed",
            "reminder_seconds",
        ]
