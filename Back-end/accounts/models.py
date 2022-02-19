from django.db import models
from django.contrib.auth.base_user import (
    AbstractBaseUser,
    BaseUserManager
)

class UserManager(BaseUserManager):
    def create_superuser(self, firstname, lastname, email, gender, city, state, date_born, password):
        if not email:
            raise ValueError('Usuario deve possuir endereço de email.')
        user = self.model(email=self.normalize_email(email)) # validação do email
        user.firstname = firstname
        user.lastname = lastname
        user.gender = gender
        user.city = city
        user.state = state
        user.date_born = date_born
        user.admin = True
        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractBaseUser):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    gender = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    date_born = models.DateField()
    last_activity = models.DateTimeField(auto_now=True)
    admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'gender', 'city', 'state', 'date_born']
    objects = UserManager()

    def __str__(self):
        return self.firstname + ' ' + self.lastname
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def get_full_name(self):
        return self.firstname + ' ' + self.lastname

    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin 
    
    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.admin
    
    
    
    