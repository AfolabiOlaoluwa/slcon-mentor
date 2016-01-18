# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin

# Register your models here.
from .models import Interest, Member, MemberLink, Project, ProjectLink, Skill

admin.site.register(Interest)
admin.site.register(Member)
admin.site.register(MemberLink)
admin.site.register(Project)
admin.site.register(ProjectLink)
admin.site.register(Skill)
