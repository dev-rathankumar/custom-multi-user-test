from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import random

# Image compression
from io import BytesIO
from PIL import Image
from django.core.files import File

from smart_selects.db_fields import ChainedForeignKey

# Custom user model
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

# User model
class User(AbstractBaseUser):
    is_customer     = models.BooleanField(default=False)
    is_business     = models.BooleanField(default=False)
    is_regional_manager     = models.BooleanField(default=False)
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50)


    # required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=False)
    is_superadmin        = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class Customer(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    customer_location     = models.CharField(max_length=100)
    customer_pin_code     = models.CharField(max_length=20)

    def __str__(self):
        return self.user.first_name

class Business(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    business_company_name = models.CharField(max_length=100)
    business_city         = models.CharField(max_length=20)

    def __str__(self):
        return self.user.first_name


# def create_id():
#     # code to generate id
#     _id = Auto.objects.latest('customer_id')
#     _id += int(1)
#     return f"CUST{_id}"

class Auto(models.Model):
    # customer_id = models.CharField(primary_key=True, max_length=20, default=create_id)

    customer_id = models.AutoField(primary_key=True, editable=True)

    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name


def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image

class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    customer_id = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='media', blank='True')

    # Override save method
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super(GeeksModel, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.weight > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        self.customer_id = 'CUST'+str(random.randint(1000,9999))+str(self.id)
        super(GeeksModel, self).save(*args, **kwargs)


class Continent(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Country(models.Model):
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Location(models.Model):
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    country = ChainedForeignKey(
        Country,
        chained_field="continent",
        chained_model_field="continent",
        show_all=False,
        auto_choose=True,
        sort=True)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
