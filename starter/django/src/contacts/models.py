from django.db import models

# Create your models here.

class Contact(models.Model):
    """Contact model
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    company = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(max_length=300, null=True, blank=True)
