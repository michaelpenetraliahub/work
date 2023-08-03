from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.



class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
    

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=254, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True, blank=True)
    is_staff = models.BooleanField(default=False, blank=True)
    date_joined = models.DateTimeField(auto_now=True , blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip() or self.email

    def get_short_name(self):
        return self.email
     
    


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=300)
    
    
 
 
class Team(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images")   
    
    
    

class Blog(models.Model):
    image = models.ImageField(upload_to="images", null=True)
    title = models.CharField(max_length=200, null=True)
    news = models.TextField(max_length=700, null=True)
    

class List_Blog(models.Model):
    image = models.ImageField(upload_to='images',null=True)
    title = models.TextField(max_length=700, null=True)  
    time = models.DateTimeField(null=True)
    
    
class Form(models.Model):
    name = models.CharField(max_length=300, null=True)
    gender = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(unique=True, null=True)
    program =models.CharField(max_length=200, null=True)
    commite = models.CharField(max_length=200,null=True) 
    source = models.CharField(max_length=200, null=True)
    employ = models.CharField(max_length=200, null=True)
    current_employ = models.CharField(max_length=200, null=True)   
    tech = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    nationality = models.CharField(max_length=200, null=True)
    option = models.CharField(max_length=300, null=True)
    industry = models.CharField(max_length=200, null=True)
    expectation = models.CharField(max_length=300, null=True)
    hear = models.CharField(max_length=200, null=True)
    