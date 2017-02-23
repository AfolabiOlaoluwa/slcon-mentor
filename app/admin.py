# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin

# Register your models here.
from .models import (Interest, Member, MemberLink, MemberSkill, Mentorship,
                     Project, ProjectLink, Skill)


class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User information', {'fields': ['first_name', 'last_name', 'email', 'location']}),
        ('Mentorship information', {'fields': ['role', 'interests']}),
        ('Login information', {'fields': ['password', 'last_login']}),
    ]


admin.site.register(Interest)
admin.site.register(Member, MemberAdmin)
admin.site.register(MemberLink)
admin.site.register(MemberSkill)
admin.site.register(Mentorship)
admin.site.register(Project)
admin.site.register(ProjectLink)
admin.site.register(Skill)
