from unicodedata import name
from django.test import TestCase
from .models import *
# Create your tests here.


class unittest(TestCase):
    def test_1_usernamenotgiven(self):
        self.assertRaises(ValueError, user.objects.create_user,
                          name="", email="ali@gmail.com", roleid='user', password="password456")

    def test_2_checksuperuser(self):
        with self.assertRaisesMessage(ValueError, 'Super user must have is_staff true'):
            user.objects.create_superuser(
                name="name", email="ali@gmail.com", roleid='user', password="password456", is_staff=False)

  
