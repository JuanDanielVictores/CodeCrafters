from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.TextField(null=True, blank=True, verbose_name='Nombres')
    last_name = models.TextField(null=True, blank=True, verbose_name='Apellidos')
    username = models.CharField(max_length=150, unique=True, verbose_name='Username')
    dni = models.TextField(unique=True, verbose_name='Número de cédula')
    email = models.EmailField(unique=True, verbose_name='Email')
    is_active = models.BooleanField(default=True, verbose_name='Estado')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Fecha de creacion')

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f'{self.first_name.upper()} {self.last_name.upper()}'

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-id']
