from django.db import models
from user_auth.models import CustomUser

class BlogPost(models.Model):
    MENTAL_HEALTH = 'Mental Health'
    HEART_DISEASE = 'Heart Disease'
    COVID_19 = 'Covid19'
    IMMUNIZATION = 'Immunization'

    CATEGORY_CHOICES = [
        (MENTAL_HEALTH, 'Mental Health'),
        (HEART_DISEASE, 'Heart Disease'),
        (COVID_19, 'Covid19'),
        (IMMUNIZATION, 'Immunization'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)  # Allow user field to be nullable
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images/')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    summary = models.TextField()
    content = models.TextField()
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title
