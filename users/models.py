from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from django.contrib.auth.base_user import BaseUserManager
from helper.models import BaseModel


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not extra_fields.get('is_superuser'):
            if not email:
                raise ValueError('Email for user must be set.')
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save()
            return user
        else:
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save()
            return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser,BaseModel):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name="_user_permissions"
    )
    joined_date = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    
    def __str__(self):
        return f"{self.email}"
