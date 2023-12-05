import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

from django.utils.translation import gettext_lazy as _

from .custom_validators import validate_phone_number

class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        if not phone_number:
            raise ValueError(_('The Phone Number field must be set'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email=email, phone_number=phone_number, password=password, **extra_fields)




class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True, validators=[validate_phone_number], max_length=11)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']


    def __str__(self):
        return self.email