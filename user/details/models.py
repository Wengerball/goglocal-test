from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pan_card_number = models.CharField(max_length=10, unique=True)
