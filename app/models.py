from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Interest(models.Model):
    """Represents a Member's Interest"""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Link(models.Model):
    """Links model. Abstract Base Class"""

    name = models.CharField(max_length=100)
    url = models.URLField()

    # This model will then not be used to create any database table
    class Meta:
        abstract = True

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Skill(models.Model):
    """Skill model"""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Member(AbstractBaseUser):
    """Member model"""

    ROLES = (
        (0, 'Mentee'),
        (1, 'Mentor'),
    )

    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    role = models.PositiveSmallIntegerField(choices=ROLES)
    interests = models.ManyToManyField(Interest)

    def __str__(self):
        return self.username


@python_2_unicode_compatible
class Project(models.Model):
    """Project model"""

    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(Member)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class MemberSkill(models.Model):
    """MemberSkill model"""

    skill = models.ForeignKey(Skill)
    member = models.ForeignKey(Member)
    # Optional field
    rating = models.PositiveSmallIntegerField(blank=True)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class MemberLink(Link):
    """Member Links model"""

    member = models.ForeignKey(Member)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ProjectLink(Link):
    """Project Links model"""

    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name
