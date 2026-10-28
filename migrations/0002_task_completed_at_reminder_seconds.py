from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="completed_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="task",
            name="reminder_seconds",
            field=models.PositiveIntegerField(
                default=30,
                help_text="30 seconds to 10 days (in seconds).",
                validators=[
                    django.core.validators.MinValueValidator(30),
                    django.core.validators.MaxValueValidator(864000),
                ],
            ),
        ),
        migrations.RemoveField(
            model_name="task",
            name="reminder_minutes",
        ),
    ]
