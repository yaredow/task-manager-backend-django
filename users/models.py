# users/models.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager  # Import the CustomUserManager
from cuid import cuid


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(
        primary_key=True,
        max_length=36,
        default=cuid,
        editable=False,
    )
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Set the custom manager
    objects = CustomUserManager()

    # Define USERNAME_FIELD as email
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email
