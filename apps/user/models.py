from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    ROLE = (

        ('SE', 'SOFT_ENGINEER'),
        ('HE', 'HARD_ENGINEER'),
    )

    TYPE_USER = (

        ('C', 'CUSTOMER'),
        ('E', 'ENGINEER')
    )
    username = None
    email = models.EmailField(('email address'), unique=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    city = models.CharField(max_length=200, blank=True, null=True)
    work_role = models.CharField(max_length=50, choices=ROLE, blank=True, null=True)
    role_user = models.CharField(max_length=50, choices=TYPE_USER, blank=True, null=True)

    def __str__(self):
        return self.email

    # def get_absolute_url(self):
    #     return reverse('user-detail', kwargs={'pk': self.pk})
    #
    # def get_work_role_id_url(self):
    #     return reverse('work_role_id', kwargs={'pk': self.pk})
    #
    # def get_role_user_id_url(self):
    #     return reverse('role_user_id', kwargs={'pk': self.pk})
