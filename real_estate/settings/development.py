from .base import *

DATABASES = {
    'default': {
        'ENGINE':env("POSTGRE_ENGINE"),
        'NAME': env("POSTGRE_DB"),
        'USER':env("POSTGRE_USER"),
        "PASSWORD":env("POSTGRE_PASSWORD"),
        "HOST":env("PG_HOST"),
        "PORT":env("PG_PORT")
    }
}
