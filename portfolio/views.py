from django.http import HttpResponse
from django.shortcuts import render

from .models import *
from .forms import ContactForm


def index(request):
    form = ContactForm
    if request.method == "POST":
        form = ContactForm(request.POST)
        if not form.is_valid():
            return HttpResponse("No")
        form.save()
        return HttpResponse("Yes")
    skills = Skill.objects.filter(is_active=True).all()
    projects = Project.objects.filter(is_active=True).all()
    context = {"skills": skills, "projects": projects, "form": form}

    return render(request, "./portfolio/index.html", context=context)
