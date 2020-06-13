from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Category(models.Model):
    category_id = models.AutoField
    status = models.BooleanField(default=True)
    name = models.CharField(max_length=50)
    img = models.ImageField(default="")
    slug = models.SlugField(max_length=300, default=name)
    desc = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Image(models.Model):
    image_id = models.AutoField
    category_id = models.ForeignKey(Category, default="", on_delete=models.CASCADE)
    img = models.ImageField(default="")

class Video(models.Model):
    video_id = models.AutoField
    category_id = models.ForeignKey(Category, default="", on_delete=models.CASCADE)
    videourl = models.URLField(max_length=250)

class User(AbstractUser):
    #email = models.EmailField(verbose_name='email',max_length=255,unique=True)
    phone = models.IntegerField(blank=True,null=True)
    REQUIRED_FIELDS = ['phone', 'first_name', 'last_name']
    #USERNAME_FIELD = 'email'

    def get_username(self):
        return self.username

class Event(models.Model):
    organiser_id = models.AutoField
    status = models.BooleanField(default=True)
    user_id = models.ForeignKey(User, default="", on_delete=models.CASCADE)
    organiser_name = models.CharField(max_length=50)
    notes = models.CharField(max_length=300)
    budget = models.IntegerField(default=0)
    contact_number = models.IntegerField(blank=True, null=True)
    dateandtime = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.organiser_name

class Testmonial(models.Model):
    testmonial_id = models.AutoField
    description = models.CharField(max_length=500, default="")
    organisereventid = models.ForeignKey(Event, default="", on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=5,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
     )

class ImageTestmonial(models.Model):
    image_id = models.AutoField
    testmonial_id = models.ForeignKey(Testmonial, default="", on_delete=models.CASCADE)
    img = models.ImageField(default="")
