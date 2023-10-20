from django.http import HttpResponse
from django.shortcuts import render

from .models import *
from .forms import ContactForm


def index(request):
    form = ContactForm
    if request.method == "POST":
        print(request.POST)
        return HttpResponse("Yes")
    skills = Skill.objects.all()
    projects = Project.objects.all()
    context = {"skills": skills, "projects": projects, "form": form}

    return render(request, "./portfolio/index.html", context=context)
