from django.shortcuts import render, get_object_or_404
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.decorators import login_required


@login_required()
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {"list_projects": projects}
    return render(request, "projects/list.html", context)


@login_required()
def show_project(request, id):
    project = get_object_or_404(Project, id=id, owner=request.user)
    tasks = project.tasks.all()
    context = {"show_project": project, "tasks": tasks}
    return render(request, "projects/detail.html", context)
