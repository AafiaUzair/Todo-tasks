from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]
    CATEGORY_CHOICES = [
        ("work", "Work"),
        ("personal", "Personal"),
        ("study", "Study"),
        ("health", "Health"),
        ("shopping", "Shopping"),
        ("other", "Other"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(
        max_length=100, choices=CATEGORY_CHOICES, blank=True
    )
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="medium")
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    reminder_seconds = models.PositiveIntegerField(
        default=30,
        validators=[MinValueValidator(30), MaxValueValidator(864000)],
        help_text="30 seconds to 10 days (in seconds).",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
