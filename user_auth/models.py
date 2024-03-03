from django.db import models
from django.contrib.auth.models import AbstractUser

# models.py

class CustomUser(AbstractUser):
    user_types = [('patient', 'Patient'), ('doctor', 'Doctor')]
    user_type = models.CharField(max_length=10, choices=user_types)
    first_name = models.CharField(max_length=30, default='null')
    last_name = models.CharField(max_length=30,default='null')
    profile_picture = models.ImageField(upload_to='profile_pics/', null=False, blank=False)
    email=models.EmailField(blank=True, null=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)



    def get_profile_picture_url(self):
        if self.profile_picture:
            return self.profile_picture.url
        return None


    def __str__(self):
        return self.username
