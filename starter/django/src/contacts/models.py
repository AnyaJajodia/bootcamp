from django.db import models

# Create your models here.

# ORM Object Relational Model

class Contact(models.Model):
    """Contact model
    """
    # Required
    name = models.CharField(max_length=100) # 255
    email = models.EmailField()
    mobile = models.CharField(max_length=25)
    # Optional
    company = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(max_length=300, null=True, blank=True)

    def check_is_duplicate(self):
        return Contact.objects.where(email=self.email, mobile=self.mobile).exists()


