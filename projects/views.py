from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm


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


@login_required()
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save
            return redirect("list_projects")
    else:
        form = ProjectForm()
        context = {"form": form}
        return render(request, "projects/create.html", context)
