from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


@python_2_unicode_compatible
class Interest(models.Model):
    """ Represents a Member's Interest
        This should be a broad field rather than a specific skill
        e.g. Design Concepts rather than Photoshop
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Skill(models.Model):
    """ Skill model """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Member(AbstractBaseUser):
    """ Member model """

    ROLES = (
        (0, 'Mentee'),
        (1, 'Mentor'),
    )

    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    location = models.CharField(max_length=100, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLES)
    interests = models.ManyToManyField(Interest)
    mentorship = models.ManyToManyField('self', through='Mentorship',
                                           symmetrical=False,
                                           related_name='+')

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.username

    def add_mentor(self, mentor, skills):
        mentorship = Mentorship.objects.get_or_create(
            mentor=mentor,
            mentee=self,
            skills=skills)
        return mentorship

    def add_mentee(self, mentee, skills):
        mentorship = Mentorship.objects.get_or_create(
            mentor=self,
            mentee=mentee,
            skills=skills)
        return mentorship

    def get_mentees(self):
        return self.mentorships.filter(mentees__mentor=self)

    def get_mentors(self):
        return self.mentorships.filter(mentors__mentee=self)

    def __str__(self):
        return self.username


class Mentorship(models.Model):
    """ Represents the Mentor-Mentee Relationship """

    mentor = models.ForeignKey(Member, related_name='mentors')
    mentee = models.ForeignKey(Member, related_name='mentees')
    # Represents the skills for which the mentorship is being done
    skills = models.ForeignKey(Skill)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)


@python_2_unicode_compatible
class Project(models.Model):
    """ Project model """

    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(Member)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class MemberSkill(models.Model):
    """ MemberSkill model """

    RATINGS = (
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Competent'),
        (4, 'Highly Experienced'),
        (5, 'Proficient'),
    )

    skill = models.ForeignKey(Skill)
    member = models.ForeignKey(Member)
    # Optional field
    rating = models.PositiveSmallIntegerField(choices=RATINGS, blank=True)

    def __str__(self):
        return '{}: {} - {}'.format(self.member, self.skill, self.rating)


@python_2_unicode_compatible
class MemberLink(models.Model):
    """ Member Links model """

    LINK_CATEGORIES = (
        (0, 'Social'),
        (1, 'Professional'),
        (2, 'Website / Blog'),
        (3, 'Other'),
    )

    member = models.ForeignKey(Member)
    category = models.PositiveSmallIntegerField(choices=LINK_CATEGORIES)
    url = models.URLField()

    def __str__(self):
        return '{} - {}'.format(self.member, self.url)


@python_2_unicode_compatible
class ProjectLink(models.Model):
    """ Project Links model """

    PROJECT_CATEGORIES = (
        (0, 'Repository'),
        (1, 'Live App'),
        (2, 'Download Link'),
        (3, 'Other'),
    )

    project = models.ForeignKey(Project)
    category = models.PositiveSmallIntegerField(choices=PROJECT_CATEGORIES)
    url = models.URLField()

    def __str__(self):
        return '{} - {}'.format(self.project, self.url)
