import uuid
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.db import models

class User(AbstractBaseUser,PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True,editable=False)
    id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    username = models.CharField(max_length=255,unique=True,verbose_name=_("Username"),help_text=_("should be a unique username"))
    first_name = models.CharField(max_length=50, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=50, verbose_name=_("Last name"))
    email = models.EmailField(unique=True,verbose_name=_("Email Adress"),help_text=_("should be a unique email"))
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS=["username",'first_name','last_name']

    objects = CustomUserManager()

    class Meta:
        verbose_name =_( "User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_short_name(self):
        return self.username