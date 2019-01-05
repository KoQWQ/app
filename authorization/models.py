# from __future__ import unicode_literals
# from django.db import models
# from django.core.mail import send_mail
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.utils.translation import ugettext_lazy as _

# from .managers import UserManager


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email'), unique=True)
#     first_name = models.CharField(_('name'), max_length=30, blank=False)
#     last_name = models.CharField(_('surname'), max_length=30, blank=False)
#     middle_name = models.CharField(_('middlename'), max_length=30, blank=True)
#     date_joined = models.DateTimeField(_('registered'), auto_now_add=True)
#     is_active = models.BooleanField(_('is_active'), default=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')

#     def get_full_name(self):
#         '''
#         Возвращает first_name и last_name с пробелом между ними.
#         '''
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()

#     def get_short_name(self):
#         '''
#         Возвращает сокращенное имя пользователя.
#         '''
#         return self.first_name

#     def email_user(self, subject, message, from_email=None, **kwargs):
#         '''
#         Отправляет электронное письмо этому пользователю.
#         '''
#         send_mail(subject, message, from_email, [self.email], **kwargs)

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()