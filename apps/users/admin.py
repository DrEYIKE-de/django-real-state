from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAmin
from django.utils.translation import gettext_lazy as _
from .forms import UserCreationForm,UserChangeForm
from .models import User

class UserAdmin(BaseUserAmin):
    ordering=["email"]
    model= User
    add_form=UserCreationForm
    form=UserChangeForm
    list_display=['pkid','id','username','email','first_name','last_name','is_active','is_staff']
    list_display_links=['id','username']
    list_filter=["email",'is_active','username','first_name','last_name']
    fieldsets = (
        (_("Login Credentials"), {
            "fields": ('email',"password",),
        },
        ),
        (
            _("Personal Information"),{
                "fields":('first_name','last_name','username',)
            },
        
        ),
        (
            _("Permissions and Groups"),{
                "fields":("is_staff","is_active","is_superuser","groups",'user_permissions',)
            },),
        (
            _("Important Date"),{
                "fields":(
                    "last_login","date_joined"
               ,),
        },),
    )
    add_fieldsets=(
        None,{
            "classes":("wide",),
            "fields":("email","password1","password2",'is_active','is_staff')
        },
    )
    search_fields=["email","username","firstname",'last_name']
    
admin.site.register(User,UserAdmin)

