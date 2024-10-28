from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.


class User(AbstractUser):
    phone = models.CharField('Phone number', max_length=20, null=True)
    avatar = models.ImageField('Avatar', upload_to='avatar', blank=True,   validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])])
    REQUIRED_FIELDS = []