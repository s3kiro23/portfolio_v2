from multiprocessing import context
from django.shortcuts import render

from . import models

def index(request):
    if request.method == 'POST':
        pass
    skills = models.Skill.objects.all()
    projects = models.Project.objects.all()
    context = { "skills": skills, "projects": projects }

    return render(request, './portfolio/index.html', context=context)