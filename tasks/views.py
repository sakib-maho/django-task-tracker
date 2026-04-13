from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


def task_list(request):
    status_filter = request.GET.get("status")
    tasks = Task.objects.all()
    if status_filter in {Task.Status.TODO, Task.Status.IN_PROGRESS, Task.Status.DONE}:
        tasks = tasks.filter(status=status_filter)

    return render(
        request,
        "tasks/task_list.html",
        {"tasks": tasks, "status_filter": status_filter or ""},
    )


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form, "mode": "Create"})


def task_update(request, pk: int):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_form.html", {"form": form, "mode": "Update"})


def task_delete(request, pk: int):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, "tasks/task_delete.html", {"task": task})


def task_detail(request, pk: int):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task})


def api_task_list(request):
    tasks = Task.objects.all()
    payload = [
        {
            **model_to_dict(task, fields=["id", "title", "description", "status", "priority", "due_date"]),
            "created_at": task.created_at.isoformat(),
            "updated_at": task.updated_at.isoformat(),
        }
        for task in tasks
    ]
    return JsonResponse({"data": payload})
