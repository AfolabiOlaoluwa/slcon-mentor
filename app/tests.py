from django.db.utils import IntegrityError
from django.test import TestCase

from .models import Member, Mentorship

class MentorshipModelTest(TestCase):
     def test_mentor_mentee_relationship_is_unique(self):
        mentor = Member.objects.create_user(email='mentor@example.com', role=1, password='123456789')
        mentee = Member.objects.create_user(email='mentee@example.com', role=0, password='123456789')

        # Create the first Mentorship object
        mentorship_1 = Mentorship.objects.create(mentor=mentor, mentee=mentee)

        # Re-create the same Mentorship relationship and check that it raises an error
        with self.assertRaises(IntegrityError):
            mentorship_2 = Mentorship.objects.create(mentor=mentor, mentee=mentee)
