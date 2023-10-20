from django.contrib import admin
from .models import *


class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "percent",
        "created_at",
        "updated_at",
    )


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "subtitle",
        "description",
        "url",
        "created_at",
        "updated_at",
    )


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "firstname",
        "lastname",
        "email",
        "message",
        "created_at",
        "updated_at",
    )


admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)
