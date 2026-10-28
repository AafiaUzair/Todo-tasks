from datetime import timedelta

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import TaskForm, UserRegisterForm
from .models import Task


def _format_remaining(delta):
    total_seconds = int(delta.total_seconds())
    if total_seconds <= 0:
        return "0s"
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    if days:
        return f"{days}d {hours}h"
    if hours:
        return f"{hours}h {minutes}m"
    if minutes:
        return f"{minutes}m {seconds}s"
    return f"{seconds}s"


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("task_list")
    else:
        form = UserRegisterForm()
    return render(request, "tasks/register.html", {"form": form})


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    query = request.GET.get("q", "").strip()
    status = request.GET.get("status", "").strip()
    priority = request.GET.get("priority", "").strip()

    if query:
        tasks = tasks.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(category__icontains=query)
        )

    if priority in {"low", "medium", "high"}:
        tasks = tasks.filter(priority=priority)

    now = timezone.now()
    if status == "completed":
        tasks = tasks.filter(completed=True)
    elif status == "pending":
        tasks = tasks.filter(completed=False)
    elif status in {"overdue", "delayed"}:
        tasks = tasks.filter(completed=False, due_date__lt=now)

    tasks = tasks.order_by("due_date", "created_at")

    reminder_tasks = []
    for task in tasks:
        if task.completed or not task.due_date:
            continue
        reminder_time = task.due_date - timedelta(seconds=task.reminder_seconds)
        if reminder_time <= now:
            reminder_tasks.append(task)

    for task in tasks:
        if task.completed:
            task.remaining_text = "Completed"
        elif not task.due_date:
            task.remaining_text = "-"
        else:
            due_local = timezone.localtime(task.due_date)
            now_local = timezone.localtime(now)
            task.remaining_text = _format_remaining(due_local - now_local)

    stats = {
        "completed": Task.objects.filter(user=request.user, completed=True).count(),
        "pending": Task.objects.filter(user=request.user, completed=False).count(),
        "overdue": Task.objects.filter(
            user=request.user, completed=False, due_date__lt=now
        ).count(),
    }

    context = {
        "tasks": tasks,
        "reminder_tasks": reminder_tasks,
        "query": query,
        "status": status,
        "priority": priority,
        "stats": stats,
        "now": now,
    }
    return render(request, "tasks/task_list.html", context)


@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form, "action": "Create"})


@login_required
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_form.html", {"form": form, "action": "Update"})


@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(
        request, "tasks/task_confirm_delete.html", {"task": task}
    )


@login_required
def task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.completed = True
        task.completed_at = timezone.now()
        task.save()
    return redirect("task_list")
