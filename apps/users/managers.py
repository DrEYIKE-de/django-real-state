from locale import normalize
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):

    def validator_email(self,email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Users must submit a correct email"))

    def create_user(self,username,first_name,last_name,email,password,**extrafields):
        if not username:
            raise ValueError(_("Users must submit a username"))
        if not first_name:
            raise ValueError(_("Users must submit a first_name"))
        if not last_name:
            raise ValueError(_("Users must submit a last_name"))
        if email:
            email = self.normalize_email(email)
            self.validator_email(email)
        else:
            raise ValueError(_("Users must submit a email"))

        user =self.model(username=username,first_name=first_name,last_name=last_name,email=email,**extrafields)

        user.set_password(password)
        extrafields.setdefault("is_staff",False)
        extrafields.setdefault("is_superuser",False)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,first_name,last_name,email,password,**extrafields):
        extrafields.setdefault("is_superuser",True)
        extrafields.setdefault("is_staff",True)
        extrafields.setdefault("is_active",True)
        if extrafields.get("is_superuser") is not True:
            raise ValueError(_("SuperUsers must have a super_user=True"))
        if extrafields.get("is_staff") is not True:
            raise ValueError(_("SuperUsers must have a is_staff=True"))
        if not password :
            raise ValueError(_("SuperUsers must have a password"))
        if email:
            email = self.normalize_email(email)
            self.validator_email(email)
        else:
            raise ValueError(_("super user required email "))
        
        user = self.create_user(username,first_name,last_name,email,password,**extrafields)
        user.save(using=self._db)
        return user
            
