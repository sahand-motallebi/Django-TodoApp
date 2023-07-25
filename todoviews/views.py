from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from .forms import TaskUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views import View

from .models import Task

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todoviews/list_task.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title"]
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy("task_list")
    form_class = TaskUpdateForm
    template_name = "todoviews/update_task.html"


class TaskComplete(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("task_list")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.complete = True
        object.save()
        return redirect(self.success_url)


@login_required
def deleteTask(request, pk):
    item = get_object_or_404(Task, id=pk, user=request.user)
    item.delete()
    return redirect("/")
