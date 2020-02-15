from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.


class MyUserManager(BaseUserManager):
    """ user manager for class """

    def create_user(self, email, username, password=None):
        """ user creating method """

        if not email:
            raise ValuError("User must have an email address ")

        user = self.model(
                
                email = email, username=username
                )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """ create superuser functions """

        user = self.create_user(email, username, password)

        user.is_admin=True
        user.is_staff=True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    """ overriding base user """

    email = models.EmailField(verbose_name='Email Address', max_length=255, unique=True)
    username = models.CharField(max_length=255)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS= ['username']

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

