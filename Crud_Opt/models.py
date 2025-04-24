from django.db import models
from django.core.validators import RegexValidator
import uuid

class Plan(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=500)  
    place = models.CharField(max_length=500)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Enter a valid phone number. Example: +8801XXXXXXXXX')
    phone = models.CharField(validators=[phone_regex], max_length=16, unique=True)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'