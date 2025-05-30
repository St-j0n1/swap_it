from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username must be set")
        if not email:
            raise ValueError("The Email must be set")

        email = self.normalize_email(email)  # Standardizes casing, domain, etc.
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)

        if 'recovery_question_answer' in extra_fields:
            user.recovery_question_answer = make_password(extra_fields['recovery_question_answer'])

        user.date_joined = timezone.now()
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not password:
            raise ValueError("Superusers must have a password")
        return self.create_user(username=username, email=email, password=password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    confirm_email = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
    last_active = models.DateField(auto_now=True)
    deals_done = models.IntegerField(default=0)
    password = models.CharField(max_length=128)
    recovery_question = models.CharField(max_length=225)
    recovery_question_answer = models.CharField(max_length=128)
    location = models.CharField(max_length=225)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'birth_date', 'email']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username