from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.html import format_html

from .managers import UserManager


class User(PermissionsMixin, AbstractBaseUser):
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(
        max_length=255,
        null=True, blank=True,
        unique=True,
    )
    full_name = models.CharField(max_length=40, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='user_profile_image')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):

        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):

        return self.is_admin

    def show_image(self):
        if self.profile_image:
            return format_html(f'<img src="{self.profile_image.url}" alt="" width="50px" height="50px">')
        else:
            return format_html('dont have a profile')

    show_image.short_description = 'profile image'
